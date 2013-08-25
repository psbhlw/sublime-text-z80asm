import sublime, sublime_plugin
import os

# Consts
THIS_PLUGIN_NAME = 'z80asm'
THIS_PLUGIN_DEBUG = True

A80_DIR=os.path.join(sublime.packages_path(), THIS_PLUGIN_NAME)
A80_SYNTAX_FILE='Packages'+'/'+THIS_PLUGIN_NAME+'/'+THIS_PLUGIN_NAME+'.tmLanguage'
A80_SNIP_DIR='Packages'+'/'+THIS_PLUGIN_NAME+'/'+'snippets'
A80_HELP_DIR=A80_DIR+'/'+'helps'


# Debug print
def dbgprint(s):
	if THIS_PLUGIN_DEBUG:
		print "Z80 Asm:",s
		sublime.status_message(s)



# Command handler class
class A80DoCmdCommand(sublime_plugin.WindowCommand):
	# Run emulator
	def emul(self):
		fn=self.window.active_view().file_name()
		if not fn:
			dbgprint("No filename specified")
			return False
		pl=sublime.platform()
		if pl=="windows": emulscr=A80_DIR+'/'+'emul.bat'
		elif pl=="linux": emulscr=A80_DIR+'/'+'emul.sh'
		elif pl=="osx": emulscr=A80_DIR+'/'+'emul'
		else:
			dbgprint("Unknown platform")
			return False

		folder_name,file_name=os.path.split(fn)
		self.window.run_command('exec',
			{'cmd': [emulscr, file_name],
			'working_dir': folder_name,
			'quiet': False})
		return True


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
			dbgprint("Build called")

		elif cmd=="Run":
			if self.emul():
				dbgprint("Emulator started")
			else:
				dbgprint("Emulator failed")

		elif cmd=="Build_Run":
			self.window.run_command("build")
			dbgprint("Build called")
			if self.emul():
				dbgprint("Emulator started")
			else:
				dbgprint("Emulator failed")

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



dbgprint("Z80 Asm plugin started!")
