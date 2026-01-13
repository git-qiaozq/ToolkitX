#!/usr/bin/env python3
"""
Maven 项目转换脚本

将 Java 项目转换为标准 Maven 结构，具有以下功能：
1. 创建标准 Maven 目录结构（src/main/java、src/test/java 等）
2. 将现有 Java 文件移动到适当的 Maven 目录
3. 将 'test' 包名替换为 'example'
4. 更新源文件中的包声明
5. 生成或更新 pom.xml
"""

import os
import re
import shutil
import sys
from pathlib import Path
from typing import List, Dict, Set
import xml.etree.ElementTree as ET
from xml.dom import minidom


class MavenConverter:
    def __init__(self, project_path: str, dry_run: bool = False):
        self.project_path = Path(project_path).resolve()
        self.dry_run = dry_run
        self.maven_structure = {
            'src/main/java': [],
            'src/main/resources': [],
            'src/test/java': [],
            'src/test/resources': []
        }
        self.moved_files: List[Dict[str, str]] = []

    def log(self, message: str):
        """打印日志信息"""
        prefix = "[预演模式] " if self.dry_run else ""
        print(f"{prefix}{message}")

    def find_java_files(self) -> List[Path]:
        """查找项目中的所有 Java 文件"""
        java_files = []
        for root, dirs, files in os.walk(self.project_path):
            # 跳过现有的 Maven 结构和构建目录
            dirs[:] = [d for d in dirs if d not in ['.git', 'target', 'build', 'out', '.idea']]

            for file in files:
                if file.endswith('.java'):
                    java_files.append(Path(root) / file)
        return java_files

    def find_resource_files(self) -> List[Path]:
        """查找资源文件（properties、xml 等）"""
        resource_extensions = {'.properties', '.xml', '.yml', '.yaml', '.json', '.txt'}
        resource_files = []

        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in ['.git', 'target', 'build', 'out', '.idea', 'src']]

            for file in files:
                if any(file.endswith(ext) for ext in resource_extensions):
                    # 排除 pom.xml 和构建文件
                    if file not in ['pom.xml', 'build.gradle', 'build.xml']:
                        resource_files.append(Path(root) / file)
        return resource_files

    def extract_package_from_file(self, file_path: Path) -> str:
        """从 Java 文件中提取包声明"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'^\s*package\s+([\w.]+)\s*;', content, re.MULTILINE)
                if match:
                    return match.group(1)
        except Exception as e:
            self.log(f"警告：无法读取 {file_path}: {e}")
        return ""

    def is_test_file(self, file_path: Path) -> bool:
        """判断 Java 文件是否为测试文件"""
        content = ""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            pass

        # 检查测试指示符
        test_indicators = [
            '@Test',
            'import org.junit',
            'import org.testng',
            'extends TestCase',
            'Test' in file_path.name
        ]

        return any(indicator in content for indicator in test_indicators)

    def convert_package_name(self, package: str) -> str:
        """将包名从 'test' 转换为 'example'"""
        # 在包名中将 'test' 替换为 'example'
        # 处理情况如：test.*、*.test.*、*.test
        parts = package.split('.')
        converted_parts = ['example' if part == 'test' else part for part in parts]
        return '.'.join(converted_parts)

    def determine_maven_path(self, file_path: Path, package: str, is_test: bool) -> Path:
        """确定文件的 Maven 标准路径"""
        # 将包转换为路径
        package_path = package.replace('.', '/')

        # 在路径中将 'test' 转换为 'example'
        package_path = package_path.replace('/test/', '/example/')
        if package_path.startswith('test/'):
            package_path = 'example/' + package_path[5:]
        if package_path.endswith('/test'):
            package_path = package_path[:-4] + 'example'
        if package_path == 'test':
            package_path = 'example'

        # 确定基础路径
        if is_test:
            base = self.project_path / 'src' / 'test' / 'java'
        else:
            base = self.project_path / 'src' / 'main' / 'java'

        return base / package_path / file_path.name

    def update_package_declaration(self, file_path: Path):
        """更新 Java 文件中的包声明"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 查找并替换包声明
            def replace_package(match):
                old_package = match.group(1)
                new_package = self.convert_package_name(old_package)
                if old_package != new_package:
                    self.log(f"  更新包名：{old_package} -> {new_package}")
                return f"package {new_package};"

            new_content = re.sub(
                r'^\s*package\s+([\w.]+)\s*;',
                replace_package,
                content,
                flags=re.MULTILINE
            )

            if not self.dry_run and new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

        except Exception as e:
            self.log(f"更新 {file_path} 时出错：{e}")

    def create_maven_structure(self):
        """创建 Maven 标准目录结构"""
        self.log("创建 Maven 目录结构...")

        for dir_path in self.maven_structure.keys():
            full_path = self.project_path / dir_path
            if not self.dry_run:
                full_path.mkdir(parents=True, exist_ok=True)
            self.log(f"  已创建：{dir_path}")

    def move_java_files(self):
        """将 Java 文件移动到 Maven 结构"""
        self.log("\n分析并移动 Java 文件...")

        java_files = self.find_java_files()

        for java_file in java_files:
            # 如果已在 Maven 结构中则跳过
            if 'src/main/java' in str(java_file) or 'src/test/java' in str(java_file):
                continue

            package = self.extract_package_from_file(java_file)
            is_test = self.is_test_file(java_file)

            # 确定目标路径
            if package:
                target_path = self.determine_maven_path(java_file, package, is_test)
            else:
                # 没有包声明 - 放在相应目录的根目录
                base = 'src/test/java' if is_test else 'src/main/java'
                target_path = self.project_path / base / java_file.name

            self.log(f"  {java_file.relative_to(self.project_path)} -> {target_path.relative_to(self.project_path)}")

            if not self.dry_run:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(java_file), str(target_path))

            self.moved_files.append({
                'from': str(java_file),
                'to': str(target_path),
                'type': 'test' if is_test else 'main'
            })

    def move_resource_files(self):
        """将资源文件移动到 Maven 结构"""
        self.log("\n移动资源文件...")

        resource_files = self.find_resource_files()

        for resource_file in resource_files:
            # 尝试判断是否为测试资源
            is_test_resource = 'test' in str(resource_file).lower()

            base = 'src/test/resources' if is_test_resource else 'src/main/resources'
            target_path = self.project_path / base / resource_file.name

            self.log(f"  {resource_file.relative_to(self.project_path)} -> {target_path.relative_to(self.project_path)}")

            if not self.dry_run:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                if target_path.exists():
                    self.log(f"    警告：{target_path.name} 已存在，跳过")
                else:
                    shutil.copy2(str(resource_file), str(target_path))

    def update_package_declarations(self):
        """更新所有包声明，将 'test' 替换为 'example'"""
        self.log("\n更新包声明...")

        java_files = list((self.project_path / 'src').rglob('*.java'))

        for java_file in java_files:
            self.update_package_declaration(java_file)

    def generate_pom_xml(self, group_id: str = "com.example", artifact_id: str = None, version: str = "1.0-SNAPSHOT"):
        """生成或更新 pom.xml"""
        pom_path = self.project_path / 'pom.xml'

        if pom_path.exists():
            self.log("\npom.xml 已存在，跳过生成")
            self.log("  您可能需要手动更新 pom.xml 中的包引用")
            return

        if artifact_id is None:
            artifact_id = self.project_path.name

        self.log(f"\n生成 pom.xml...")

        pom_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>{group_id}</groupId>
    <artifactId>{artifact_id}</artifactId>
    <version>{version}</version>
    <packaging>jar</packaging>

    <name>{artifact_id}</name>
    <description>由 maven-converter 生成的 Maven 项目</description>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <junit.version>5.9.2</junit.version>
    </properties>

    <dependencies>
        <!-- JUnit 5 -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>${{junit.version}}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>${{junit.version}}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>${{maven.compiler.source}}</source>
                    <target>${{maven.compiler.target}}</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0</version>
            </plugin>
        </plugins>
    </build>
</project>
'''

        if not self.dry_run:
            with open(pom_path, 'w', encoding='utf-8') as f:
                f.write(pom_content)

        self.log(f"  已生成：pom.xml")
        self.log(f"    groupId: {group_id}")
        self.log(f"    artifactId: {artifact_id}")
        self.log(f"    version: {version}")

    def cleanup_empty_dirs(self):
        """转换后删除空目录"""
        self.log("\n清理空目录...")

        for root, dirs, files in os.walk(self.project_path, topdown=False):
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                # 跳过 Maven 结构和特殊目录
                if 'src' in str(dir_path) or dir_name in ['.git', '.idea']:
                    continue
                try:
                    if not any(dir_path.iterdir()):
                        if not self.dry_run:
                            dir_path.rmdir()
                        self.log(f"  已删除空目录：{dir_path.relative_to(self.project_path)}")
                except:
                    pass

    def convert(self, group_id: str = "com.example", artifact_id: str = None, version: str = "1.0-SNAPSHOT"):
        """执行完整的 Maven 转换"""
        self.log(f"{'='*60}")
        self.log(f"Maven 项目转换器")
        self.log(f"项目：{self.project_path}")
        self.log(f"{'='*60}\n")

        # 创建 Maven 结构
        self.create_maven_structure()

        # 移动文件
        self.move_java_files()
        self.move_resource_files()

        # 更新包声明
        self.update_package_declarations()

        # 生成 pom.xml
        self.generate_pom_xml(group_id, artifact_id, version)

        # 清理
        self.cleanup_empty_dirs()

        self.log(f"\n{'='*60}")
        self.log(f"转换{'模拟' if self.dry_run else '完成'}！")
        self.log(f"已移动 {len(self.moved_files)} 个 Java 文件")
        self.log(f"{'='*60}")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='将 Java 项目转换为 Maven 标准结构'
    )
    parser.add_argument(
        'project_path',
        nargs='?',
        default='.',
        help='项目目录路径（默认：当前目录）'
    )
    parser.add_argument(
        '--group-id',
        default='com.example',
        help='Maven groupId（默认：com.example）'
    )
    parser.add_argument(
        '--artifact-id',
        help='Maven artifactId（默认：项目目录名）'
    )
    parser.add_argument(
        '--version',
        default='1.0-SNAPSHOT',
        help='项目版本（默认：1.0-SNAPSHOT）'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='模拟转换而不进行实际更改'
    )

    args = parser.parse_args()

    converter = MavenConverter(args.project_path, dry_run=args.dry_run)
    converter.convert(
        group_id=args.group_id,
        artifact_id=args.artifact_id,
        version=args.version
    )


if __name__ == '__main__':
    main()
