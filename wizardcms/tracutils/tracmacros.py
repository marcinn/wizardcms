from trac.wiki.macros import WikiMacroBase

class SubPagesMacro(WikiMacroBase):
    def expand_macro(self, formatter, name, args):
        return "Subpages!"

