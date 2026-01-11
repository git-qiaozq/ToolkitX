# Full Replication Prompt (English Version)

Act as an expert frontend creative developer specializing in **Three.js**, **WebGL**, and **Computer Vision (MediaPipe Hands)**. Your task is to create a high-performance, single-file HTML application featuring a cyberpunk interactive particle system.
**Visual Style:**
* **Theme:** Hardcore Cyberpunk.
* **Background:** Deep black with subtle moving grid/scanlines and a vignette effect.
* **HUD:** Minimalist data display in the four corners (FPS, Particle Count, Hand Status), using the `Orbitron` or monospaced font in Neon Cyan.
* **Material:** Particles must use `AdditiveBlending` for a glowing, neon look.
**Core Parameters:**
* **Particle Count:** 12,000.
* **Particle Size:** 2.4.
* **Physics:** Fast return speed (lerp factor 0.16). Strong and snappy repulsion force.
**Interaction Logic (Detailed Requirements):**
**1. 👋 Left Hand (Command Controller):**
Detect the number of extended fingers to switch the target shape and color of the particles:
* **1 Finger:** Text **"Hello"** | Color: **Neon Blue** (0x00FFFF).
* **2 Fingers:** Text **"Gemini3"** | Color: **Neon Yellow** (0xFFFF00).
* **3 Fingers:** Text **"非常好用"** (Chinese for "Very Useful") | Color: **Neon Pink** (0xFF00FF).
* **4 Fingers:** Text **"再见"** (Chinese for "Goodbye") | Color: **Neon Green** (0x00FF88).
* **5 Fingers (Open Palm):** Enter **"Catch Mode"** (acts as a destination container).
**2. Right Hand (Physics Interactor):**
* **Tracking Point:** Always track the **Index Finger Tip** (Landmark 8).
* **State A (Pointing/Fist - Default):**
* Interaction: When touching text particles, trigger a **Strong Scatter** effect.
* Constraint: Pure planar repulsion (XY axis). **Do NOT** apply any Z-axis bulge or distortion (keep it flat).

* **State B (Open Hand - 5 Fingers):**
* Trigger: **Nebula Mode**. Particles scatter to fill the entire screen 3D space.
* Interaction: Applying a **Water Ripple** (sine wave) effect when the hand moves through the particles.
**3. Dual Hand Combo (Ultimate Effect):**
* **Condition:** When **Right Hand is Open** (Nebula active) **AND** **Left Hand is Open** (Catch active) simultaneously.
* **Effect Logic:**
* All full-screen particles are instantly attracted to the **Left Hand Palm center**.
* **Shape:** Particles form a **Rotating 3D Basketball** in the left hand (Orange color, using Fibonacci sphere distribution, with calculated black lines to simulate ball texture).
* **Motion Trajectory:** Particles must fly towards the left hand with a **Bouncing/Jumping trajectory** (high-frequency Y-axis sine wave), looking like thousands of energetic bouncing beads.
**Technical Implementation:**
* Use `Canvas` pixel scanning to generate text coordinates (Font size: 75px, bold).
* Configure MediaPipe Hands to detect a maximum of 2 hands.
* No mobile-specific constraints (use default webcam settings).
* Ensure the code is self-contained in a single `index.html` file (CSS, JS, HTML combined).
