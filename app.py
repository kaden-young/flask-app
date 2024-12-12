from flask import Flask, render_template

app = Flask(__name__)

# List of images to cycle through
images = ["square_xsml_map-7.png", "wide_med_20191024-diercks-hall-exteriors-12.jpg", "wide_xlrg_20201115-building-exteriors-kern-center-21.jpg"]

# A simple index to track which image to show next
current_index = 0

@app.route('/')
def index():
    global current_index
    # Get the current image
    img = images[current_index]
    
    # Move to the next index, wrap around using modulo
    current_index = (current_index + 1) % len(images)
    
    return render_template("index.html", image=img)

if __name__ == '__main__':
    app.run(debug=True)
