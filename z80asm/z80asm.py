import sublime, sublime_plugin
import os

# Consts
THIS_PLUGIN_NAME = 'z80asm'
THIS_PLUGIN_DEBUG = True

# Initialize plugin
def A80Init():
	global A80_DIR, A80_SYNTAX_FILE, A80_SNIP_DIR, A80_HELP_DIR
	A80_DIR=os.path.join(sublime.packages_path(), THIS_PLUGIN_NAME)
	A80_SYNTAX_FILE='Packages'+'/'+THIS_PLUGIN_NAME+'/'+THIS_PLUGIN_NAME+'.tmLanguage'
	A80_SNIP_DIR='Packages'+'/'+THIS_PLUGIN_NAME+'/'+'snippets'
	A80_HELP_DIR=A80_DIR+'/'+'helps'



# Debug print
def dbgprint(s):
	if THIS_PLUGIN_DEBUG:
		print ("Z80 Asm:",s)
		sublime.status_message(s)



# Command handler class
class A80DoCmdCommand(sublime_plugin.WindowCommand):
	# Command handler
	def run(self, cmd):

		if cmd=="NewCode":
			v=self.window.new_file()
			v.set_syntax_file(A80_SYNTAX_FILE)
			v.run_command("insert_snippet", {"name": A80_SNIP_DIR+'/init.sublime-snippet'})
			dbgprint("New Code created")

		elif cmd=="NewBasic":
			v=self.window.new_file()
			v.set_syntax_file(A80_SYNTAX_FILE)
			v.run_command("insert_snippet", {"name": A80_SNIP_DIR+'/basic.sublime-snippet'})
			dbgprint("New Basic loader created")

		elif cmd=="Build":
			self.window.run_command("build")
			dbgprint("Build started")

		elif cmd=="Run":
			self.window.run_command("build", {"variant": "Run"})
			dbgprint("Emulator started")

		elif cmd=="Build_Run":
			self.window.run_command("build", {"variant": "Build and Run"})
			dbgprint("Build and Run script started")

		elif cmd=="AFormat":
			dbgprint("Not implemented yet")

		elif cmd=="JLine":
			dbgprint("Not implemented yet")

		elif cmd=="Sline":
			dbgprint("Not implemented yet")

		elif cmd=="SynStorm":
			dbgprint("Not implemented yet")

		elif cmd=="SynAlasm":
			dbgprint("Not implemented yet")


	# Disable not implemented items
	def is_enabled(self, cmd):
		if cmd not in ["AFormat", "JLine", "Sline", "SynStorm", "SynAlasm"]:
			return True
		return False



# Helps
class A80HelpCommand(sublime_plugin.WindowCommand):
	def run(self, indx):
		n=self.help_list()
		self.window.run_command("open_file", {"file": "${packages}/z80asm/helps/"+n[indx]})

	# Scan helps folder for files (10 max)
	def help_list(self):
		lst=os.listdir(A80_HELP_DIR)
		lst.sort()
		return lst[:10]

	# Show help
	def is_visible(self, indx):
		n=self.help_list()
		if indx<len(n):
			return True
		return False

	# Show help names
	def description(self, indx):
		n=self.help_list()
		if indx<len(n):
			return n[indx]
		return ""



# Quick help - F1
class A80QuickHelpCommand(sublime_plugin.WindowCommand):
	# Init: read items from file
	def __init__(self, *args, **kwargs):
		self.help=[]
		with open(A80_DIR+'/'+THIS_PLUGIN_NAME+'.quickhelp','rt') as f:
			self.help = [line.strip() for line in f]

		super(A80QuickHelpCommand,self).__init__(*args, **kwargs)

	# Show help
	def run(self):
		self.window.show_quick_panel(self.help, None, sublime.MONOSPACE_FONT)



# Autocompletion class
class A80Autocomplete(sublime_plugin.EventListener):
	# Generate completion list from all opened tabs
	def on_query_completions(self, view, prefix, locations):
		# Check if option is enabled
		if view.settings().get("use_global_completion") != True:
			return []

		# List of all views (our one is always first)
		views = [view] + [v for v in sublime.active_window().views() if v.id() != view.id()]
		compl=[]
		for v in views:
			if v.id() == view.id():
				# For our view use cursor location
				words = v.extract_completions(prefix,locations[0])
			else:
				words = v.extract_completions(prefix)
			# Add only unique words
			for w in words:
				if w not in compl:
					compl.append(w)

		return [(el, el) for el in compl]



# Define plugin_loaded() function for ST3 because it's have another plugin lifecycle
# (cannot call sublime.packages_path() at importing time). For ST2 fust call A80Init().
if int(sublime.version())>=3000:
	def plugin_loaded():
		A80Init()
else:
	A80Init()

dbgprint("Z80 Asm plugin started!")
