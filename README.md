# NKT Ratio Fractal Simulator

#### Description:
Hello World! Here is the Python rookie again :) \
This is a farewell gift I created for my math teacher, **NKT** (initials used to protect their privacy), who is leaving our school. \
It uses basic mathematical formulas to draw an **Iterated Function System (IFS)** fractal pattern that eventually assembles into the letters "NKT". \
Since I am a secondary school student, the script is small and straightforward, but it does its work perfectly to show my gratitude. \
I think the program could be displayed even more beautifully if I used `matplotlib`, which I haven't learned yet but am definitely willing to learn next!

<br>
<br>

## Project Structure
*   **`main.py`**: The application file containing the drawing logic, zoom event handlers, and window configurations.

<br>
<br>

## Function List
*   **`printone(k)`**: Draws a static set of "NKT" letters at a specific scale \(k\).
*   **`forwardprintone(n1, K1)`**: Calculates and repeats `printone` for a certain inputted scale `n1` unit of `K1`.
*   **`printtwo(k2)`**: Uses `forwardprintone` to print the pattern again with a higher dimension ratio.
*   **`fprinttwo(fk2)`**: Functions identically to `printtwo` but introduces a corner gap to display the smaller recursive structures properly.
*   **`handle_scroll(event)`**: Detects mouse wheel inputs to scale the zoom variable `v`.
*   **`game_loop()`**: Clears the canvas, updates pen thickness, and loops every 16ms using a timer. It achieves a fractal visual effect by rendering two different sizes of the pattern simultaneously; when zoomed in close enough, the lower-dimension (simplified) pattern is replaced by the higher-dimension one.
*   **`main()`**: Turns off manual screen tracing, binds the scroll wheel, and boots up the game.

<br>
<br>

## Design Choice & Philosophy

### 1. The Scroll Wheel Zoom Reset
During testing, I realized that infinite scrolling would cause the math variables to become too massive or tiny, leading to lag. To prevent this, I added a boundary system using `math.isclose()` to detect when the zoom reaches its maximum limit (\(1.1^{31}\)):

```python
if event.delta > 0:
    if v > 1 * (1.1**31) or math.isclose(v, 1 * (1.1**31)):
        v = 1
    else:
        v *= 1.1
```
The script wraps the zoom level back around to 1 instead of stopping, creating a seamless loop for the viewer.

<br>
<br>

### 2. Dynamic Pen Thickness
Using a static pen size made the lines look incredibly thick and messy when zooming in closely. To keep the lines crisp, I modified the loop to dynamically alter the thickness based on the zoom factor `v`:

```python
pensize(2 * (v * 0.1 + 0.9))
```
This guarantees that the shapes remain legible at any distance.

<br>
<br>

### 3. Video Game Render Optimization Concept
To mimic a true fractal depth without exploding the computer's CPU, the game loop renders two different detail scales at the same time. As the user zooms close enough, the lower-dimension, simplified pattern is hot-swapped and replaced by the higher-dimension, detailed pattern. This operates exactly like Level of Detail (LOD) rendering techniques used in modern video games—achieving a decent infinite visual effect while saving critical calculation power.

<br>
<br>

### 4. Integrating Live Math Text
Because this project is a gift for a math teacher, I used the `write()` function to print the exact fractional dimension equation directly onto the canvas as an educational detail:

$$\text{Dimension} = \frac{\log(N)}{\log(1/r)} = \frac{\log(82)}{\log(21)} \approx 1.447$$

This bridges the gap between coding art and pure mathematical theory.

<br>
<br>

## Installation & Setup

### Python Packages
This project relies purely on standard Python libraries. You do not need to install any external dependencies.
*   `turtle` (Built-in standard library)
*   `math` (Built-in standard library)

<br>
<br>

## How to Run & Controls
1. Run the game using:
   ```bash
   python main.py
   ```
2. A window titled **"NKT fractal"** will appear.
3. **Controls**: Use your **Mouse Scroll Wheel** anywhere on the canvas to zoom in and out of the "NKT" fractal geometry in real-time.

---
*Thank you, NKT, for being a wonderful math teacher! Best wishes for your next journey!*
