from gi.repository import Gtk, GObject, RB, Peas

menuui_string = """
<ui>
    <menubar name="MenuBar">
        <menu name="ControlMenu" action="Control">
            <menuitem name="StopAfterCurrentTrack" action="StopAfterCurrentTrack"/>
        </menu>
    </menubar>
</ui>
"""

class StopAfterCurrentTrackPlugin (GObject.Object, Peas.Activatable):
    object = GObject.property(type=GObject.Object)

    def __init__(self):
        super(StopAfterCurrentTrackPlugin, self).__init__()

    def do_activate(self):
        self.stop_status = False
        shell = self.object
        self.action = Gtk.Action(
                name='StopAfterCurrentTrack',
                label=('Stop After Current Track'),
                tooltip=('Stop playback after current song'),
                stock_id='media-stop'
                )
        self.activate_id = self.action.connect('activate',self.toggle_status,shell)
        self.action_group = Gtk.ActionGroup(name='StopAfterCurrentTrackPluginActions')
        self.action_group.add_action(self.action)

        uim = shell.props.ui_manager
        uim.insert_action_group(self.action_group,0)
        self.ui_id = uim.add_ui_from_string(menuui_string)
        uim.ensure_update()

    def do_deactivate(self):
        shell = self.object
        uim = shell.props.ui_manager
        uim.remove_ui(self.ui_id)
        uim.remove_action_group(self.action_group)
        self.action_group = None
        self.action = None
        self.stop_status = None

    def toggle_status(self,action,shell):
        self.stop_status = not self.stop_status
        print "Status Toggled"

