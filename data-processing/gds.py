import gdsfactory as gf

# Create a new component
c = gf.Component()

# Add a rectangle
rect = c.add_ref(gf.components.rectangle(size=(10, 10), layer=(1, 0)))

# Add text elements
text1 = c.add_ref(gf.components.text("Hello", size=10, layer=(2, 0)))
text2 = c.add_ref(gf.components.text("world", size=10, layer=(2, 0)))

# Position elements
text1.xmin = rect.xmax + 5
text2.xmin = text1.xmax + 2
text2.rotate(30)

# Show the result
c.show()