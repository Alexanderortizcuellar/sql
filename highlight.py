import re
from PyQt5 import QtGui, QtWidgets, QtCore

class PythonHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)

        self.highlightingRules = []

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkBlue)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)
        keywords = ["select", "and", "from", "drop", "insert"]
        for keyword in keywords:
            pattern = re.compile("\\b" + keyword + "\\b")
            rule = HighlightingRule(pattern, keywordFormat)
            self.highlightingRules.append(rule)

        self.stringFormat = QtGui.QTextCharFormat()
        self.stringFormat.setForeground(QtCore.Qt.red)
        self.stringFormat.setFontWeight(QtGui.QFont.Normal)
        self.stringRule = HighlightingRule(re.compile(r'"[^"]*"'), self.stringFormat)
        self.highlightingRules.append(self.stringRule)

        self.singleQuoteFormat = QtGui.QTextCharFormat()
        self.singleQuoteFormat.setForeground(QtCore.Qt.red)
        self.singleQuoteFormat.setFontWeight(QtGui.QFont.Normal)
        self.singleQuoteRule = HighlightingRule(re.compile(r"'[^']*'"), self.singleQuoteFormat)
        self.highlightingRules.append(self.singleQuoteRule)

        self.numberFormat = QtGui.QTextCharFormat()
        self.numberFormat.setForeground(QtCore.Qt.magenta)
        self.numberRule = HighlightingRule(re.compile(r'\b[0-9]+\b'), self.numberFormat)
        self.highlightingRules.append(self.numberRule)

    def highlightBlock(self, text):
        for rule in self.highlightingRules:
            match = rule.pattern.match(text)
            while match:
                index = match.start()
                length = match.end() - match.start()
                self.setFormat(index, length, rule.format)
                match = rule.pattern.match(text, index + length)

class HighlightingRule():
    def __init__(self, pattern, format):
        self.pattern = pattern
        self.format = format

app = QtWidgets.QApplication([])
editor = QtWidgets.QPlainTextEdit()
highlighter = PythonHighlighter(editor.document())
editor.show()
app.exec_()

def name():
    return 
