# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01f4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\5\2\u0094\n\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\7\27\u010d\n\27\f\27\16\27\u0110\13\27\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u0116\n\30\3\31\3\31\3\31\7\31\u011b\n\31\f")
        buf.write("\31\16\31\u011e\13\31\5\31\u0120\n\31\3\32\3\32\3\32\3")
        buf.write("\32\5\32\u0126\n\32\3\32\6\32\u0129\n\32\r\32\16\32\u012a")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u0131\n\33\3\33\6\33\u0134\n")
        buf.write("\33\r\33\16\33\u0135\3\34\3\34\3\34\3\34\5\34\u013c\n")
        buf.write("\34\3\34\6\34\u013f\n\34\r\34\16\34\u0140\3\35\6\35\u0144")
        buf.write("\n\35\r\35\16\35\u0145\3\35\3\35\7\35\u014a\n\35\f\35")
        buf.write("\16\35\u014d\13\35\3\35\5\35\u0150\n\35\3\36\3\36\3\37")
        buf.write("\3\37\5\37\u0156\n\37\3\37\6\37\u0159\n\37\r\37\16\37")
        buf.write("\u015a\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&")
        buf.write("\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3=\3>\3")
        buf.write(">\3?\3?\3?\7?\u01aa\n?\f?\16?\u01ad\13?\3?\3?\3?\3@\3")
        buf.write("@\3A\3A\3A\3B\3B\3B\3C\6C\u01bb\nC\rC\16C\u01bc\3C\3C")
        buf.write("\3D\3D\3D\3D\7D\u01c5\nD\fD\16D\u01c8\13D\3D\3D\3E\3E")
        buf.write("\3E\3E\3E\7E\u01d1\nE\fE\16E\u01d4\13E\3E\3E\3E\3E\3E")
        buf.write("\3F\3F\3F\7F\u01de\nF\fF\16F\u01e1\13F\3F\5F\u01e4\nF")
        buf.write("\3F\3F\3G\3G\3G\7G\u01eb\nG\fG\16G\u01ee\13G\3G\3G\3G")
        buf.write("\3H\3H\5\u01ab\u01d2\u01ec\2I\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\2=\2?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c")
        buf.write("\61e\62g\63i\64k\65m\66o\67q8s9u:w;y<{=}>\177\2\u0081")
        buf.write("\2\u0083?\u0085@\u0087A\u0089B\u008bC\u008dD\u008fE\3")
        buf.write("\2\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62\63\3\2")
        buf.write("\629\5\2\62;CHch\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\7")
        buf.write("\2$$^^ppttvv\5\2\13\13\16\17\"\"\3\2\f\f\4\2\f\f\16\16")
        buf.write("\2\u020c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2")
        buf.write("\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2")
        buf.write("\u008f\3\2\2\2\3\u0093\3\2\2\2\5\u0095\3\2\2\2\7\u0098")
        buf.write("\3\2\2\2\t\u009d\3\2\2\2\13\u00a2\3\2\2\2\r\u00a8\3\2")
        buf.write("\2\2\17\u00ac\3\2\2\2\21\u00b2\3\2\2\2\23\u00b8\3\2\2")
        buf.write("\2\25\u00c1\3\2\2\2\27\u00c8\3\2\2\2\31\u00cd\3\2\2\2")
        buf.write("\33\u00d2\3\2\2\2\35\u00d9\3\2\2\2\37\u00e3\3\2\2\2!\u00e7")
        buf.write("\3\2\2\2#\u00ee\3\2\2\2%\u00f2\3\2\2\2\'\u00f8\3\2\2\2")
        buf.write(")\u0100\3\2\2\2+\u0106\3\2\2\2-\u010a\3\2\2\2/\u0115\3")
        buf.write("\2\2\2\61\u011f\3\2\2\2\63\u0125\3\2\2\2\65\u0130\3\2")
        buf.write("\2\2\67\u013b\3\2\2\29\u0143\3\2\2\2;\u0151\3\2\2\2=\u0153")
        buf.write("\3\2\2\2?\u015c\3\2\2\2A\u015e\3\2\2\2C\u0160\3\2\2\2")
        buf.write("E\u0162\3\2\2\2G\u0164\3\2\2\2I\u0166\3\2\2\2K\u0169\3")
        buf.write("\2\2\2M\u016c\3\2\2\2O\u016f\3\2\2\2Q\u0172\3\2\2\2S\u0175")
        buf.write("\3\2\2\2U\u0178\3\2\2\2W\u017b\3\2\2\2Y\u017d\3\2\2\2")
        buf.write("[\u017f\3\2\2\2]\u0182\3\2\2\2_\u0185\3\2\2\2a\u0187\3")
        buf.write("\2\2\2c\u018a\3\2\2\2e\u018d\3\2\2\2g\u018f\3\2\2\2i\u0191")
        buf.write("\3\2\2\2k\u0193\3\2\2\2m\u0195\3\2\2\2o\u0197\3\2\2\2")
        buf.write("q\u0199\3\2\2\2s\u019b\3\2\2\2u\u019d\3\2\2\2w\u019f\3")
        buf.write("\2\2\2y\u01a1\3\2\2\2{\u01a4\3\2\2\2}\u01a6\3\2\2\2\177")
        buf.write("\u01b1\3\2\2\2\u0081\u01b3\3\2\2\2\u0083\u01b6\3\2\2\2")
        buf.write("\u0085\u01ba\3\2\2\2\u0087\u01c0\3\2\2\2\u0089\u01cb\3")
        buf.write("\2\2\2\u008b\u01da\3\2\2\2\u008d\u01e7\3\2\2\2\u008f\u01f2")
        buf.write("\3\2\2\2\u0091\u0094\5\t\5\2\u0092\u0094\5\13\6\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094\4\3\2\2\2\u0095")
        buf.write("\u0096\7k\2\2\u0096\u0097\7h\2\2\u0097\6\3\2\2\2\u0098")
        buf.write("\u0099\7g\2\2\u0099\u009a\7n\2\2\u009a\u009b\7u\2\2\u009b")
        buf.write("\u009c\7g\2\2\u009c\b\3\2\2\2\u009d\u009e\7v\2\2\u009e")
        buf.write("\u009f\7t\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1\7g\2\2\u00a1")
        buf.write("\n\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7c\2\2\u00a4")
        buf.write("\u00a5\7n\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7\7g\2\2\u00a7")
        buf.write("\f\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7q\2\2\u00aa")
        buf.write("\u00ab\7t\2\2\u00ab\16\3\2\2\2\u00ac\u00ad\7t\2\2\u00ad")
        buf.write("\u00ae\7c\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7i\2\2\u00b0")
        buf.write("\u00b1\7g\2\2\u00b1\20\3\2\2\2\u00b2\u00b3\7d\2\2\u00b3")
        buf.write("\u00b4\7t\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7c\2\2\u00b6")
        buf.write("\u00b7\7m\2\2\u00b7\22\3\2\2\2\u00b8\u00b9\7e\2\2\u00b9")
        buf.write("\u00ba\7q\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7v\2\2\u00bc")
        buf.write("\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7w\2\2\u00bf")
        buf.write("\u00c0\7g\2\2\u00c0\24\3\2\2\2\u00c1\u00c2\7t\2\2\u00c2")
        buf.write("\u00c3\7g\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7w\2\2\u00c5")
        buf.write("\u00c6\7t\2\2\u00c6\u00c7\7p\2\2\u00c7\26\3\2\2\2\u00c8")
        buf.write("\u00c9\7h\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7p\2\2\u00cb")
        buf.write("\u00cc\7e\2\2\u00cc\30\3\2\2\2\u00cd\u00ce\7v\2\2\u00ce")
        buf.write("\u00cf\7{\2\2\u00cf\u00d0\7r\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write("\32\3\2\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4\7v\2\2\u00d4")
        buf.write("\u00d5\7t\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7\7e\2\2\u00d7")
        buf.write("\u00d8\7v\2\2\u00d8\34\3\2\2\2\u00d9\u00da\7k\2\2\u00da")
        buf.write("\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write("\u00de\7t\2\2\u00de\u00df\7h\2\2\u00df\u00e0\7c\2\2\u00e0")
        buf.write("\u00e1\7e\2\2\u00e1\u00e2\7g\2\2\u00e2\36\3\2\2\2\u00e3")
        buf.write("\u00e4\7x\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7t\2\2\u00e6")
        buf.write(" \3\2\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7v\2\2\u00e9")
        buf.write("\u00ea\7t\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7p\2\2\u00ec")
        buf.write("\u00ed\7i\2\2\u00ed\"\3\2\2\2\u00ee\u00ef\7k\2\2\u00ef")
        buf.write("\u00f0\7p\2\2\u00f0\u00f1\7v\2\2\u00f1$\3\2\2\2\u00f2")
        buf.write("\u00f3\7h\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5\7q\2\2\u00f5")
        buf.write("\u00f6\7c\2\2\u00f6\u00f7\7v\2\2\u00f7&\3\2\2\2\u00f8")
        buf.write("\u00f9\7d\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7q\2\2\u00fb")
        buf.write("\u00fc\7n\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7c\2\2\u00fe")
        buf.write("\u00ff\7p\2\2\u00ff(\3\2\2\2\u0100\u0101\7e\2\2\u0101")
        buf.write("\u0102\7q\2\2\u0102\u0103\7p\2\2\u0103\u0104\7u\2\2\u0104")
        buf.write("\u0105\7v\2\2\u0105*\3\2\2\2\u0106\u0107\7p\2\2\u0107")
        buf.write("\u0108\7k\2\2\u0108\u0109\7n\2\2\u0109,\3\2\2\2\u010a")
        buf.write("\u010e\t\2\2\2\u010b\u010d\t\3\2\2\u010c\u010b\3\2\2\2")
        buf.write("\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3")
        buf.write("\2\2\2\u010f.\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0116")
        buf.write("\5\61\31\2\u0112\u0116\5\65\33\2\u0113\u0116\5\63\32\2")
        buf.write("\u0114\u0116\5\67\34\2\u0115\u0111\3\2\2\2\u0115\u0112")
        buf.write("\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("\60\3\2\2\2\u0117\u0120\7\62\2\2\u0118\u011c\t\4\2\2\u0119")
        buf.write("\u011b\5;\36\2\u011a\u0119\3\2\2\2\u011b\u011e\3\2\2\2")
        buf.write("\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u0120\3")
        buf.write("\2\2\2\u011e\u011c\3\2\2\2\u011f\u0117\3\2\2\2\u011f\u0118")
        buf.write("\3\2\2\2\u0120\62\3\2\2\2\u0121\u0122\7\62\2\2\u0122\u0126")
        buf.write("\7d\2\2\u0123\u0124\7\62\2\2\u0124\u0126\7D\2\2\u0125")
        buf.write("\u0121\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0128\3\2\2\2")
        buf.write("\u0127\u0129\t\5\2\2\u0128\u0127\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\64")
        buf.write("\3\2\2\2\u012c\u012d\7\62\2\2\u012d\u0131\7Q\2\2\u012e")
        buf.write("\u012f\7\62\2\2\u012f\u0131\7q\2\2\u0130\u012c\3\2\2\2")
        buf.write("\u0130\u012e\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0134\t")
        buf.write("\6\2\2\u0133\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0133")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\66\3\2\2\2\u0137\u0138")
        buf.write("\7\62\2\2\u0138\u013c\7z\2\2\u0139\u013a\7\62\2\2\u013a")
        buf.write("\u013c\7Z\2\2\u013b\u0137\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013c\u013e\3\2\2\2\u013d\u013f\t\7\2\2\u013e\u013d\3")
        buf.write("\2\2\2\u013f\u0140\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u01418\3\2\2\2\u0142\u0144\5;\36\2\u0143\u0142")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014b\7\60\2")
        buf.write("\2\u0148\u014a\5;\36\2\u0149\u0148\3\2\2\2\u014a\u014d")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u0150\5=\37\2")
        buf.write("\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150:\3\2\2")
        buf.write("\2\u0151\u0152\t\b\2\2\u0152<\3\2\2\2\u0153\u0155\t\t")
        buf.write("\2\2\u0154\u0156\t\n\2\2\u0155\u0154\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0159\5;\36\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u0158\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015b>\3\2\2\2\u015c\u015d\7-\2\2")
        buf.write("\u015d@\3\2\2\2\u015e\u015f\7/\2\2\u015fB\3\2\2\2\u0160")
        buf.write("\u0161\7,\2\2\u0161D\3\2\2\2\u0162\u0163\7\61\2\2\u0163")
        buf.write("F\3\2\2\2\u0164\u0165\7\'\2\2\u0165H\3\2\2\2\u0166\u0167")
        buf.write("\7-\2\2\u0167\u0168\7?\2\2\u0168J\3\2\2\2\u0169\u016a")
        buf.write("\7/\2\2\u016a\u016b\7?\2\2\u016bL\3\2\2\2\u016c\u016d")
        buf.write("\7,\2\2\u016d\u016e\7?\2\2\u016eN\3\2\2\2\u016f\u0170")
        buf.write("\7\61\2\2\u0170\u0171\7?\2\2\u0171P\3\2\2\2\u0172\u0173")
        buf.write("\7\'\2\2\u0173\u0174\7?\2\2\u0174R\3\2\2\2\u0175\u0176")
        buf.write("\7?\2\2\u0176\u0177\7?\2\2\u0177T\3\2\2\2\u0178\u0179")
        buf.write("\7#\2\2\u0179\u017a\7?\2\2\u017aV\3\2\2\2\u017b\u017c")
        buf.write("\7@\2\2\u017cX\3\2\2\2\u017d\u017e\7>\2\2\u017eZ\3\2\2")
        buf.write("\2\u017f\u0180\7@\2\2\u0180\u0181\7?\2\2\u0181\\\3\2\2")
        buf.write("\2\u0182\u0183\7>\2\2\u0183\u0184\7?\2\2\u0184^\3\2\2")
        buf.write("\2\u0185\u0186\7#\2\2\u0186`\3\2\2\2\u0187\u0188\7(\2")
        buf.write("\2\u0188\u0189\7(\2\2\u0189b\3\2\2\2\u018a\u018b\7~\2")
        buf.write("\2\u018b\u018c\7~\2\2\u018cd\3\2\2\2\u018d\u018e\7*\2")
        buf.write("\2\u018ef\3\2\2\2\u018f\u0190\7+\2\2\u0190h\3\2\2\2\u0191")
        buf.write("\u0192\7]\2\2\u0192j\3\2\2\2\u0193\u0194\7_\2\2\u0194")
        buf.write("l\3\2\2\2\u0195\u0196\7}\2\2\u0196n\3\2\2\2\u0197\u0198")
        buf.write("\7\177\2\2\u0198p\3\2\2\2\u0199\u019a\7.\2\2\u019ar\3")
        buf.write("\2\2\2\u019b\u019c\7=\2\2\u019ct\3\2\2\2\u019d\u019e\7")
        buf.write("<\2\2\u019ev\3\2\2\2\u019f\u01a0\7\60\2\2\u01a0x\3\2\2")
        buf.write("\2\u01a1\u01a2\7<\2\2\u01a2\u01a3\7?\2\2\u01a3z\3\2\2")
        buf.write("\2\u01a4\u01a5\7?\2\2\u01a5|\3\2\2\2\u01a6\u01ab\7$\2")
        buf.write("\2\u01a7\u01aa\5\177@\2\u01a8\u01aa\5\u0081A\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae\3\2\2\2")
        buf.write("\u01ad\u01ab\3\2\2\2\u01ae\u01af\7$\2\2\u01af\u01b0\b")
        buf.write("?\2\2\u01b0~\3\2\2\2\u01b1\u01b2\n\13\2\2\u01b2\u0080")
        buf.write("\3\2\2\2\u01b3\u01b4\7^\2\2\u01b4\u01b5\t\f\2\2\u01b5")
        buf.write("\u0082\3\2\2\2\u01b6\u01b7\7\f\2\2\u01b7\u01b8\bB\3\2")
        buf.write("\u01b8\u0084\3\2\2\2\u01b9\u01bb\t\r\2\2\u01ba\u01b9\3")
        buf.write("\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\bC\4\2\u01bf")
        buf.write("\u0086\3\2\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c2\7\61\2")
        buf.write("\2\u01c2\u01c6\3\2\2\2\u01c3\u01c5\n\16\2\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c9\u01ca\bD\4\2\u01ca\u0088\3\2\2\2\u01cb\u01cc\7")
        buf.write("\61\2\2\u01cc\u01cd\7,\2\2\u01cd\u01d2\3\2\2\2\u01ce\u01d1")
        buf.write("\5\u0089E\2\u01cf\u01d1\13\2\2\2\u01d0\u01ce\3\2\2\2\u01d0")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d3\3\2\2\2")
        buf.write("\u01d2\u01d0\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d5\u01d6\7,\2\2\u01d6\u01d7\7\61\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01d9\bE\4\2\u01d9\u008a\3\2\2\2\u01da")
        buf.write("\u01df\7$\2\2\u01db\u01de\5\177@\2\u01dc\u01de\5\u0081")
        buf.write("A\2\u01dd\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1")
        buf.write("\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e4\t\17\2")
        buf.write("\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5")
        buf.write("\3\2\2\2\u01e5\u01e6\bF\5\2\u01e6\u008c\3\2\2\2\u01e7")
        buf.write("\u01ec\7$\2\2\u01e8\u01eb\5\177@\2\u01e9\u01eb\5\u0081")
        buf.write("A\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ee")
        buf.write("\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed")
        buf.write("\u01ef\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f0\7^\2\2")
        buf.write("\u01f0\u01f1\n\f\2\2\u01f1\u008e\3\2\2\2\u01f2\u01f3\13")
        buf.write("\2\2\2\u01f3\u0090\3\2\2\2\36\2\u0093\u010e\u0115\u011c")
        buf.write("\u011f\u0125\u012a\u0130\u0135\u013b\u0140\u0145\u014b")
        buf.write("\u014f\u0155\u015a\u01a9\u01ab\u01bc\u01c6\u01d0\u01d2")
        buf.write("\u01dd\u01df\u01e3\u01ea\u01ec\6\3?\2\3B\3\b\2\2\3F\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLITERAL = 1
    IF = 2
    ELSE = 3
    TRUE = 4
    FALSE = 5
    FOR = 6
    RANGE = 7
    BREAK = 8
    CONTINUE = 9
    RETURN = 10
    FUNC = 11
    TYPE = 12
    STRUCT = 13
    INTERFACE = 14
    VAR = 15
    STRING = 16
    INTTYPE = 17
    FLOAT = 18
    BOOLEAN = 19
    CONST = 20
    NIL = 21
    ID = 22
    INT = 23
    DECINT = 24
    BININT = 25
    OCTINT = 26
    HEXINT = 27
    REAL = 28
    ADD = 29
    MINUS = 30
    MUL = 31
    DIV = 32
    MOD = 33
    ADDAS = 34
    MiNUSAS = 35
    MULAS = 36
    DIVAS = 37
    MODAS = 38
    EQUAL = 39
    NEQUAL = 40
    BIG = 41
    SMALL = 42
    EBIG = 43
    ESMALL = 44
    NOT = 45
    AND = 46
    OR = 47
    LB = 48
    RB = 49
    LS = 50
    RS = 51
    LC = 52
    RC = 53
    COMMA = 54
    SEMI = 55
    COLON = 56
    DOT = 57
    AS1 = 58
    AS2 = 59
    STRINGLIT = 60
    NL = 61
    WS = 62
    COMMENT1 = 63
    COMMENT2 = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'true'", "'false'", "'for'", "'range'", "'break'", 
            "'continue'", "'return'", "'func'", "'type'", "'struct'", "'interface'", 
            "'var'", "'string'", "'int'", "'float'", "'boolean'", "'const'", 
            "'nil'", "'+'", "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", 
            "'*='", "'/='", "'%='", "'=='", "'!='", "'>'", "'<'", "'>='", 
            "'<='", "'!'", "'&&'", "'||'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "','", "';'", "':'", "'.'", "':='", "'='", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLITERAL", "IF", "ELSE", "TRUE", "FALSE", "FOR", "RANGE", 
            "BREAK", "CONTINUE", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "VAR", "STRING", "INTTYPE", "FLOAT", "BOOLEAN", "CONST", "NIL", 
            "ID", "INT", "DECINT", "BININT", "OCTINT", "HEXINT", "REAL", 
            "ADD", "MINUS", "MUL", "DIV", "MOD", "ADDAS", "MiNUSAS", "MULAS", 
            "DIVAS", "MODAS", "EQUAL", "NEQUAL", "BIG", "SMALL", "EBIG", 
            "ESMALL", "NOT", "AND", "OR", "LB", "RB", "LS", "RS", "LC", 
            "RC", "COMMA", "SEMI", "COLON", "DOT", "AS1", "AS2", "STRINGLIT", 
            "NL", "WS", "COMMENT1", "COMMENT2", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "BOOLITERAL", "IF", "ELSE", "TRUE", "FALSE", "FOR", "RANGE", 
                  "BREAK", "CONTINUE", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "VAR", "STRING", "INTTYPE", "FLOAT", "BOOLEAN", 
                  "CONST", "NIL", "ID", "INT", "DECINT", "BININT", "OCTINT", 
                  "HEXINT", "REAL", "DIGIT", "EXPONENT", "ADD", "MINUS", 
                  "MUL", "DIV", "MOD", "ADDAS", "MiNUSAS", "MULAS", "DIVAS", 
                  "MODAS", "EQUAL", "NEQUAL", "BIG", "SMALL", "EBIG", "ESMALL", 
                  "NOT", "AND", "OR", "LB", "RB", "LS", "RS", "LC", "RC", 
                  "COMMA", "SEMI", "COLON", "DOT", "AS1", "AS2", "STRINGLIT", 
                  "STRING_CHAR", "IllEscape", "NL", "WS", "COMMENT1", "COMMENT2", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    previous_token = None
    def emit(self):
        tk = self.type
        self.previous_token = tk
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();

    def handle(self):
        if not self.previous_token:
            return False
        auto_semi_types = [
            self.RB, self.RC, self.RS,
            self.ID, self.INT, self.REAL,
            self.BOOLITERAL, self.STRINGLIT,
            self.INTTYPE, self.FLOAT,
            self.STRING, self.BOOLEAN, self.RETURN,
            self.CONTINUE, self. BREAK, self. NIL
        ]
        if self.previous_token in auto_semi_types:
            return True
        else:
            return False


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[61] = self.STRINGLIT_action 
            actions[64] = self.NL_action 
            actions[68] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
                self.text = self.text.strip('\n')
                self.text = self.text.strip('\r')
                self.text = self.text.strip('\f')

     

    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                if self.handle():
                    self.text = ';'
                    self.type = self.SEMI
                else:
                    self.skip()

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text.strip('\n')
                self.text = self.text.strip('\r')
                self.text = self.text.strip('\f')

     


