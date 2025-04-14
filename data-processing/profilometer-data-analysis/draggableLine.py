class DraggableLine:
    def __init__(self, line, parent, index):
        self.line = line
        self.parent = parent
        self.index = index
        self.press = None
        self.cidpress = line.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = line.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = line.figure.canvas.mpl_connect('motion_notify_event', self.on_move)

    def on_press(self, event):
        if event.inaxes != self.line.axes:
            return
        contains, attrd = self.line.contains(event)
        if not contains:
            return
        if event.button == 2:  # Right-click
            self.parent.remove_line(self.index)
            return
        self.press = event.xdata

    def on_move(self, event):
        if self.press is None:
            return
        if event.inaxes != self.line.axes:
            return
        dx = event.xdata - self.press
        xdata = self.line.get_xdata()
        self.line.set_xdata(xdata + dx)
        self.press = event.xdata
        self.line.figure.canvas.draw()

    def on_release(self, event):
        self.press = None

    def disconnect(self):
        try:
            self.line.figure.canvas.mpl_disconnect(self.cidpress)
            self.line.figure.canvas.mpl_disconnect(self.cidrelease)
            self.line.figure.canvas.mpl_disconnect(self.cidmotion)
        except Exception as e:
            print(e)