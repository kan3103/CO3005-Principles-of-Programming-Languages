# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u02b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u008e\n\3\3\4\3\4\3\4\5\4")
        buf.write("\u0093\n\4\3\5\3\5\3\5\5\5\u0098\n\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00ac\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u00bc\n\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00cc\n\n\f\n\16")
        buf.write("\n\u00cf\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00d9\n\13\3\f\3\f\3\f\3\f\5\f\u00df\n\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\r\u00e7\n\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\7\20\u00fe\n\20\f\20\16\20\u0101")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u010b")
        buf.write("\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u0119\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u0121\n\25\3\26\3\26\3\26\5\26\u0126\n\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\5\33\u014c\n\33\3\34\3\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u015e\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u0167\n\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u016f")
        buf.write("\n\36\f\36\16\36\u0172\13\36\3\37\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \3 \3 \3 \7 \u017e\n \f \16 \u0181\13 \3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\7\"\u018b\n\"\f\"\16\"\u018e\13\"\3")
        buf.write("#\3#\3#\3#\3#\3#\7#\u0196\n#\f#\16#\u0199\13#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\7$\u01a2\n$\f$\16$\u01a5\13$\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\7&\u01b2\n&\f&\16&\u01b5\13&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01c3")
        buf.write("\n\'\f\'\16\'\u01c6\13\'\3(\3(\3(\3(\3(\5(\u01cd\n(\3")
        buf.write(")\3)\3)\3)\5)\u01d3\n)\3*\3*\3*\3*\3*\3*\3*\3*\3*\7*\u01de")
        buf.write("\n*\f*\16*\u01e1\13*\3+\3+\3+\3+\3+\3+\3+\5+\u01ea\n+")
        buf.write("\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0202\n\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u020e")
        buf.write("\n\61\f\61\16\61\u0211\13\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\5\62\u021b\n\62\3\63\3\63\5\63\u021f\n")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\7\66\u023f")
        buf.write("\n\66\f\66\16\66\u0242\13\66\3\67\3\67\5\67\u0246\n\67")
        buf.write("\38\38\38\38\38\38\38\38\38\38\38\78\u0253\n8\f8\168\u0256")
        buf.write("\138\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\7")
        buf.write(":\u0268\n:\f:\16:\u026b\13:\3;\3;\3;\3;\3;\3;\3;\5;\u0274")
        buf.write("\n;\3<\3<\3<\3<\3<\3<\3<\3<\5<\u027e\n<\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\5=\u0288\n=\3>\3>\5>\u028c\n>\3?\3?\3?\3?\3")
        buf.write("@\3@\3@\3@\3@\5@\u0297\n@\3A\3A\3A\3A\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\5B\u02a5\nB\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\7C\u02b1")
        buf.write("\nC\fC\16C\u02b4\13C\3C\2\21\22\36:>BDFJLR`jnr\u0084D")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\2\5\4\2\22\25\30\30\4\2$(<<\3\2).\2\u02be\2\u0086")
        buf.write("\3\2\2\2\4\u008d\3\2\2\2\6\u0092\3\2\2\2\b\u0097\3\2\2")
        buf.write("\2\n\u00ab\3\2\2\2\f\u00bb\3\2\2\2\16\u00bd\3\2\2\2\20")
        buf.write("\u00c3\3\2\2\2\22\u00c5\3\2\2\2\24\u00d8\3\2\2\2\26\u00de")
        buf.write("\3\2\2\2\30\u00e6\3\2\2\2\32\u00e8\3\2\2\2\34\u00ec\3")
        buf.write("\2\2\2\36\u00f8\3\2\2\2 \u010a\3\2\2\2\"\u010c\3\2\2\2")
        buf.write("$\u010f\3\2\2\2&\u0118\3\2\2\2(\u0120\3\2\2\2*\u0125\3")
        buf.write("\2\2\2,\u0127\3\2\2\2.\u012c\3\2\2\2\60\u0139\3\2\2\2")
        buf.write("\62\u0143\3\2\2\2\64\u014b\3\2\2\2\66\u014d\3\2\2\28\u015d")
        buf.write("\3\2\2\2:\u0166\3\2\2\2<\u0173\3\2\2\2>\u0177\3\2\2\2")
        buf.write("@\u0182\3\2\2\2B\u0184\3\2\2\2D\u018f\3\2\2\2F\u019a\3")
        buf.write("\2\2\2H\u01a6\3\2\2\2J\u01a8\3\2\2\2L\u01b6\3\2\2\2N\u01cc")
        buf.write("\3\2\2\2P\u01d2\3\2\2\2R\u01d4\3\2\2\2T\u01e9\3\2\2\2")
        buf.write("V\u01eb\3\2\2\2X\u01ee\3\2\2\2Z\u01f1\3\2\2\2\\\u01f4")
        buf.write("\3\2\2\2^\u0201\3\2\2\2`\u0203\3\2\2\2b\u021a\3\2\2\2")
        buf.write("d\u021e\3\2\2\2f\u0220\3\2\2\2h\u0226\3\2\2\2j\u022e\3")
        buf.write("\2\2\2l\u0245\3\2\2\2n\u0247\3\2\2\2p\u0257\3\2\2\2r\u025b")
        buf.write("\3\2\2\2t\u0273\3\2\2\2v\u027d\3\2\2\2x\u0287\3\2\2\2")
        buf.write("z\u028b\3\2\2\2|\u028d\3\2\2\2~\u0296\3\2\2\2\u0080\u0298")
        buf.write("\3\2\2\2\u0082\u02a4\3\2\2\2\u0084\u02a6\3\2\2\2\u0086")
        buf.write("\u0087\5\6\4\2\u0087\u0088\5\4\3\2\u0088\3\3\2\2\2\u0089")
        buf.write("\u008a\5\6\4\2\u008a\u008b\5\4\3\2\u008b\u008e\3\2\2\2")
        buf.write("\u008c\u008e\7\2\2\3\u008d\u0089\3\2\2\2\u008d\u008c\3")
        buf.write("\2\2\2\u008e\5\3\2\2\2\u008f\u0093\5\24\13\2\u0090\u0093")
        buf.write("\5\b\5\2\u0091\u0093\5d\63\2\u0092\u008f\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\7\3\2\2\2\u0094")
        buf.write("\u0098\5\f\7\2\u0095\u0098\5\n\6\2\u0096\u0098\5\16\b")
        buf.write("\2\u0097\u0094\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\t\3\2\2\2\u0099\u009a\7\21\2\2\u009a\u009b")
        buf.write("\7\30\2\2\u009b\u009c\5\20\t\2\u009c\u009d\7=\2\2\u009d")
        buf.write("\u009e\5@!\2\u009e\u009f\79\2\2\u009f\u00ac\3\2\2\2\u00a0")
        buf.write("\u00a1\7\21\2\2\u00a1\u00a2\7\30\2\2\u00a2\u00a3\5\20")
        buf.write("\t\2\u00a3\u00a4\79\2\2\u00a4\u00ac\3\2\2\2\u00a5\u00a6")
        buf.write("\7\21\2\2\u00a6\u00a7\7\30\2\2\u00a7\u00a8\7=\2\2\u00a8")
        buf.write("\u00a9\5@!\2\u00a9\u00aa\79\2\2\u00aa\u00ac\3\2\2\2\u00ab")
        buf.write("\u0099\3\2\2\2\u00ab\u00a0\3\2\2\2\u00ab\u00a5\3\2\2\2")
        buf.write("\u00ac\13\3\2\2\2\u00ad\u00ae\7\21\2\2\u00ae\u00af\7\30")
        buf.write("\2\2\u00af\u00b0\5x=\2\u00b0\u00b1\5\20\t\2\u00b1\u00b2")
        buf.write("\7=\2\2\u00b2\u00b3\5@!\2\u00b3\u00b4\79\2\2\u00b4\u00bc")
        buf.write("\3\2\2\2\u00b5\u00b6\7\21\2\2\u00b6\u00b7\7\30\2\2\u00b7")
        buf.write("\u00b8\5x=\2\u00b8\u00b9\5\20\t\2\u00b9\u00ba\79\2\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00ad\3\2\2\2\u00bb\u00b5\3\2\2\2")
        buf.write("\u00bc\r\3\2\2\2\u00bd\u00be\7\26\2\2\u00be\u00bf\7\30")
        buf.write("\2\2\u00bf\u00c0\7=\2\2\u00c0\u00c1\5@!\2\u00c1\u00c2")
        buf.write("\79\2\2\u00c2\17\3\2\2\2\u00c3\u00c4\t\2\2\2\u00c4\21")
        buf.write("\3\2\2\2\u00c5\u00c6\b\n\1\2\u00c6\u00c7\7\30\2\2\u00c7")
        buf.write("\u00cd\3\2\2\2\u00c8\u00c9\f\3\2\2\u00c9\u00ca\78\2\2")
        buf.write("\u00ca\u00cc\7\30\2\2\u00cb\u00c8\3\2\2\2\u00cc\u00cf")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\23\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7\r\2\2\u00d1")
        buf.write("\u00d2\7\30\2\2\u00d2\u00d3\5\30\r\2\u00d3\u00d4\5\26")
        buf.write("\f\2\u00d4\u00d5\5\32\16\2\u00d5\u00d6\79\2\2\u00d6\u00d9")
        buf.write("\3\2\2\2\u00d7\u00d9\5\34\17\2\u00d8\u00d0\3\2\2\2\u00d8")
        buf.write("\u00d7\3\2\2\2\u00d9\25\3\2\2\2\u00da\u00db\5z>\2\u00db")
        buf.write("\u00dc\5\20\t\2\u00dc\u00df\3\2\2\2\u00dd\u00df\3\2\2")
        buf.write("\2\u00de\u00da\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\27\3")
        buf.write("\2\2\2\u00e0\u00e1\7\62\2\2\u00e1\u00e2\5n8\2\u00e2\u00e3")
        buf.write("\7\63\2\2\u00e3\u00e7\3\2\2\2\u00e4\u00e5\7\62\2\2\u00e5")
        buf.write("\u00e7\7\63\2\2\u00e6\u00e0\3\2\2\2\u00e6\u00e4\3\2\2")
        buf.write("\2\u00e7\31\3\2\2\2\u00e8\u00e9\7\66\2\2\u00e9\u00ea\5")
        buf.write("\36\20\2\u00ea\u00eb\7\67\2\2\u00eb\33\3\2\2\2\u00ec\u00ed")
        buf.write("\7\r\2\2\u00ed\u00ee\7\62\2\2\u00ee\u00ef\7\30\2\2\u00ef")
        buf.write("\u00f0\5z>\2\u00f0\u00f1\5\20\t\2\u00f1\u00f2\7\63\2\2")
        buf.write("\u00f2\u00f3\7\30\2\2\u00f3\u00f4\5\30\r\2\u00f4\u00f5")
        buf.write("\5\26\f\2\u00f5\u00f6\5\32\16\2\u00f6\u00f7\79\2\2\u00f7")
        buf.write("\35\3\2\2\2\u00f8\u00f9\b\20\1\2\u00f9\u00fa\5 \21\2\u00fa")
        buf.write("\u00ff\3\2\2\2\u00fb\u00fc\f\3\2\2\u00fc\u00fe\5 \21\2")
        buf.write("\u00fd\u00fb\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3")
        buf.write("\2\2\2\u00ff\u0100\3\2\2\2\u0100\37\3\2\2\2\u0101\u00ff")
        buf.write("\3\2\2\2\u0102\u010b\5\62\32\2\u0103\u010b\58\35\2\u0104")
        buf.write("\u010b\5(\25\2\u0105\u010b\5\"\22\2\u0106\u010b\5$\23")
        buf.write("\2\u0107\u010b\5\b\5\2\u0108\u010b\5&\24\2\u0109\u010b")
        buf.write("\5*\26\2\u010a\u0102\3\2\2\2\u010a\u0103\3\2\2\2\u010a")
        buf.write("\u0104\3\2\2\2\u010a\u0105\3\2\2\2\u010a\u0106\3\2\2\2")
        buf.write("\u010a\u0107\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u0109\3")
        buf.write("\2\2\2\u010b!\3\2\2\2\u010c\u010d\7\13\2\2\u010d\u010e")
        buf.write("\79\2\2\u010e#\3\2\2\2\u010f\u0110\7\n\2\2\u0110\u0111")
        buf.write("\79\2\2\u0111%\3\2\2\2\u0112\u0113\7\f\2\2\u0113\u0114")
        buf.write("\5@!\2\u0114\u0115\79\2\2\u0115\u0119\3\2\2\2\u0116\u0117")
        buf.write("\7\f\2\2\u0117\u0119\79\2\2\u0118\u0112\3\2\2\2\u0118")
        buf.write("\u0116\3\2\2\2\u0119\'\3\2\2\2\u011a\u011b\5X-\2\u011b")
        buf.write("\u011c\79\2\2\u011c\u0121\3\2\2\2\u011d\u011e\5b\62\2")
        buf.write("\u011e\u011f\79\2\2\u011f\u0121\3\2\2\2\u0120\u011a\3")
        buf.write("\2\2\2\u0120\u011d\3\2\2\2\u0121)\3\2\2\2\u0122\u0126")
        buf.write("\5,\27\2\u0123\u0126\5.\30\2\u0124\u0126\5\60\31\2\u0125")
        buf.write("\u0122\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2")
        buf.write("\u0126+\3\2\2\2\u0127\u0128\7\b\2\2\u0128\u0129\5@!\2")
        buf.write("\u0129\u012a\5\32\16\2\u012a\u012b\79\2\2\u012b-\3\2\2")
        buf.write("\2\u012c\u012d\7\b\2\2\u012d\u012e\7\30\2\2\u012e\u012f")
        buf.write("\5\66\34\2\u012f\u0130\5@!\2\u0130\u0131\79\2\2\u0131")
        buf.write("\u0132\5@!\2\u0132\u0133\79\2\2\u0133\u0134\7\30\2\2\u0134")
        buf.write("\u0135\5\66\34\2\u0135\u0136\5@!\2\u0136\u0137\5\32\16")
        buf.write("\2\u0137\u0138\79\2\2\u0138/\3\2\2\2\u0139\u013a\7\b\2")
        buf.write("\2\u013a\u013b\7\30\2\2\u013b\u013c\78\2\2\u013c\u013d")
        buf.write("\7\30\2\2\u013d\u013e\7<\2\2\u013e\u013f\7\t\2\2\u013f")
        buf.write("\u0140\5@!\2\u0140\u0141\5\32\16\2\u0141\u0142\79\2\2")
        buf.write("\u0142\61\3\2\2\2\u0143\u0144\5\64\33\2\u0144\u0145\5")
        buf.write("\66\34\2\u0145\u0146\5@!\2\u0146\u0147\79\2\2\u0147\63")
        buf.write("\3\2\2\2\u0148\u014c\7\30\2\2\u0149\u014c\5V,\2\u014a")
        buf.write("\u014c\5Z.\2\u014b\u0148\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014a\3\2\2\2\u014c\65\3\2\2\2\u014d\u014e\t\3\2\2\u014e")
        buf.write("\67\3\2\2\2\u014f\u0150\7\4\2\2\u0150\u0151\5<\37\2\u0151")
        buf.write("\u0152\5\32\16\2\u0152\u0153\5:\36\2\u0153\u0154\7\5\2")
        buf.write("\2\u0154\u0155\5\32\16\2\u0155\u0156\79\2\2\u0156\u015e")
        buf.write("\3\2\2\2\u0157\u0158\7\4\2\2\u0158\u0159\5<\37\2\u0159")
        buf.write("\u015a\5\32\16\2\u015a\u015b\5:\36\2\u015b\u015c\79\2")
        buf.write("\2\u015c\u015e\3\2\2\2\u015d\u014f\3\2\2\2\u015d\u0157")
        buf.write("\3\2\2\2\u015e9\3\2\2\2\u015f\u0160\b\36\1\2\u0160\u0161")
        buf.write("\7\5\2\2\u0161\u0162\7\4\2\2\u0162\u0163\5<\37\2\u0163")
        buf.write("\u0164\5\32\16\2\u0164\u0167\3\2\2\2\u0165\u0167\3\2\2")
        buf.write("\2\u0166\u015f\3\2\2\2\u0166\u0165\3\2\2\2\u0167\u0170")
        buf.write("\3\2\2\2\u0168\u0169\f\4\2\2\u0169\u016a\7\5\2\2\u016a")
        buf.write("\u016b\7\4\2\2\u016b\u016c\5<\37\2\u016c\u016d\5\32\16")
        buf.write("\2\u016d\u016f\3\2\2\2\u016e\u0168\3\2\2\2\u016f\u0172")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write(";\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174\7\62\2\2\u0174")
        buf.write("\u0175\5@!\2\u0175\u0176\7\63\2\2\u0176=\3\2\2\2\u0177")
        buf.write("\u0178\b \1\2\u0178\u0179\5@!\2\u0179\u017f\3\2\2\2\u017a")
        buf.write("\u017b\f\3\2\2\u017b\u017c\78\2\2\u017c\u017e\5@!\2\u017d")
        buf.write("\u017a\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180?\3\2\2\2\u0181\u017f\3\2\2")
        buf.write("\2\u0182\u0183\5B\"\2\u0183A\3\2\2\2\u0184\u0185\b\"\1")
        buf.write("\2\u0185\u0186\5D#\2\u0186\u018c\3\2\2\2\u0187\u0188\f")
        buf.write("\4\2\2\u0188\u0189\7\61\2\2\u0189\u018b\5D#\2\u018a\u0187")
        buf.write("\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018dC\3\2\2\2\u018e\u018c\3\2\2\2\u018f")
        buf.write("\u0190\b#\1\2\u0190\u0191\5F$\2\u0191\u0197\3\2\2\2\u0192")
        buf.write("\u0193\f\4\2\2\u0193\u0194\7\60\2\2\u0194\u0196\5F$\2")
        buf.write("\u0195\u0192\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0197\u0198\3\2\2\2\u0198E\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u019a\u019b\b$\1\2\u019b\u019c\5J&\2\u019c\u01a3")
        buf.write("\3\2\2\2\u019d\u019e\f\4\2\2\u019e\u019f\5H%\2\u019f\u01a0")
        buf.write("\5J&\2\u01a0\u01a2\3\2\2\2\u01a1\u019d\3\2\2\2\u01a2\u01a5")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("G\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\t\4\2\2\u01a7")
        buf.write("I\3\2\2\2\u01a8\u01a9\b&\1\2\u01a9\u01aa\5L\'\2\u01aa")
        buf.write("\u01b3\3\2\2\2\u01ab\u01ac\f\5\2\2\u01ac\u01ad\7\37\2")
        buf.write("\2\u01ad\u01b2\5L\'\2\u01ae\u01af\f\4\2\2\u01af\u01b0")
        buf.write("\7 \2\2\u01b0\u01b2\5L\'\2\u01b1\u01ab\3\2\2\2\u01b1\u01ae")
        buf.write("\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4K\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6")
        buf.write("\u01b7\b\'\1\2\u01b7\u01b8\5N(\2\u01b8\u01c4\3\2\2\2\u01b9")
        buf.write("\u01ba\f\6\2\2\u01ba\u01bb\7!\2\2\u01bb\u01c3\5N(\2\u01bc")
        buf.write("\u01bd\f\5\2\2\u01bd\u01be\7\"\2\2\u01be\u01c3\5N(\2\u01bf")
        buf.write("\u01c0\f\4\2\2\u01c0\u01c1\7#\2\2\u01c1\u01c3\5N(\2\u01c2")
        buf.write("\u01b9\3\2\2\2\u01c2\u01bc\3\2\2\2\u01c2\u01bf\3\2\2\2")
        buf.write("\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3")
        buf.write("\2\2\2\u01c5M\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8")
        buf.write("\7 \2\2\u01c8\u01cd\5N(\2\u01c9\u01ca\7/\2\2\u01ca\u01cd")
        buf.write("\5N(\2\u01cb\u01cd\5P)\2\u01cc\u01c7\3\2\2\2\u01cc\u01c9")
        buf.write("\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cdO\3\2\2\2\u01ce\u01d3")
        buf.write("\5X-\2\u01cf\u01d3\5Z.\2\u01d0\u01d3\5V,\2\u01d1\u01d3")
        buf.write("\5T+\2\u01d2\u01ce\3\2\2\2\u01d2\u01cf\3\2\2\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3Q\3\2\2\2\u01d4\u01d5")
        buf.write("\b*\1\2\u01d5\u01d6\5T+\2\u01d6\u01df\3\2\2\2\u01d7\u01d8")
        buf.write("\f\5\2\2\u01d8\u01de\5\\/\2\u01d9\u01da\f\4\2\2\u01da")
        buf.write("\u01de\5^\60\2\u01db\u01dc\f\3\2\2\u01dc\u01de\5`\61\2")
        buf.write("\u01dd\u01d7\3\2\2\2\u01dd\u01d9\3\2\2\2\u01dd\u01db\3")
        buf.write("\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0S\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3")
        buf.write("\7\62\2\2\u01e3\u01e4\5@!\2\u01e4\u01e5\7\63\2\2\u01e5")
        buf.write("\u01ea\3\2\2\2\u01e6\u01ea\5t;\2\u01e7\u01ea\7\30\2\2")
        buf.write("\u01e8\u01ea\5b\62\2\u01e9\u01e2\3\2\2\2\u01e9\u01e6\3")
        buf.write("\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01eaU")
        buf.write("\3\2\2\2\u01eb\u01ec\5R*\2\u01ec\u01ed\5\\/\2\u01edW\3")
        buf.write("\2\2\2\u01ee\u01ef\5R*\2\u01ef\u01f0\5^\60\2\u01f0Y\3")
        buf.write("\2\2\2\u01f1\u01f2\5R*\2\u01f2\u01f3\5`\61\2\u01f3[\3")
        buf.write("\2\2\2\u01f4\u01f5\7;\2\2\u01f5\u01f6\7\30\2\2\u01f6]")
        buf.write("\3\2\2\2\u01f7\u01f8\7;\2\2\u01f8\u01f9\7\30\2\2\u01f9")
        buf.write("\u01fa\7\62\2\2\u01fa\u01fb\5> \2\u01fb\u01fc\7\63\2\2")
        buf.write("\u01fc\u0202\3\2\2\2\u01fd\u01fe\7;\2\2\u01fe\u01ff\7")
        buf.write("\30\2\2\u01ff\u0200\7\62\2\2\u0200\u0202\7\63\2\2\u0201")
        buf.write("\u01f7\3\2\2\2\u0201\u01fd\3\2\2\2\u0202_\3\2\2\2\u0203")
        buf.write("\u0204\b\61\1\2\u0204\u0205\7\64\2\2\u0205\u0206\5@!\2")
        buf.write("\u0206\u0207\7\65\2\2\u0207\u020f\3\2\2\2\u0208\u0209")
        buf.write("\f\3\2\2\u0209\u020a\7\64\2\2\u020a\u020b\5@!\2\u020b")
        buf.write("\u020c\7\65\2\2\u020c\u020e\3\2\2\2\u020d\u0208\3\2\2")
        buf.write("\2\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210a\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0213")
        buf.write("\7\30\2\2\u0213\u0214\7\62\2\2\u0214\u0215\5> \2\u0215")
        buf.write("\u0216\7\63\2\2\u0216\u021b\3\2\2\2\u0217\u0218\7\30\2")
        buf.write("\2\u0218\u0219\7\62\2\2\u0219\u021b\7\63\2\2\u021a\u0212")
        buf.write("\3\2\2\2\u021a\u0217\3\2\2\2\u021bc\3\2\2\2\u021c\u021f")
        buf.write("\5f\64\2\u021d\u021f\5h\65\2\u021e\u021c\3\2\2\2\u021e")
        buf.write("\u021d\3\2\2\2\u021fe\3\2\2\2\u0220\u0221\7\16\2\2\u0221")
        buf.write("\u0222\7\30\2\2\u0222\u0223\7\17\2\2\u0223\u0224\5p9\2")
        buf.write("\u0224\u0225\79\2\2\u0225g\3\2\2\2\u0226\u0227\7\16\2")
        buf.write("\2\u0227\u0228\7\30\2\2\u0228\u0229\7\20\2\2\u0229\u022a")
        buf.write("\7\66\2\2\u022a\u022b\5j\66\2\u022b\u022c\7\67\2\2\u022c")
        buf.write("\u022d\79\2\2\u022di\3\2\2\2\u022e\u022f\b\66\1\2\u022f")
        buf.write("\u0230\7\30\2\2\u0230\u0231\7\62\2\2\u0231\u0232\5l\67")
        buf.write("\2\u0232\u0233\7\63\2\2\u0233\u0234\5\26\f\2\u0234\u0235")
        buf.write("\79\2\2\u0235\u0240\3\2\2\2\u0236\u0237\f\3\2\2\u0237")
        buf.write("\u0238\7\30\2\2\u0238\u0239\7\62\2\2\u0239\u023a\5l\67")
        buf.write("\2\u023a\u023b\7\63\2\2\u023b\u023c\5\26\f\2\u023c\u023d")
        buf.write("\79\2\2\u023d\u023f\3\2\2\2\u023e\u0236\3\2\2\2\u023f")
        buf.write("\u0242\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u0241\3\2\2\2")
        buf.write("\u0241k\3\2\2\2\u0242\u0240\3\2\2\2\u0243\u0246\5n8\2")
        buf.write("\u0244\u0246\3\2\2\2\u0245\u0243\3\2\2\2\u0245\u0244\3")
        buf.write("\2\2\2\u0246m\3\2\2\2\u0247\u0248\b8\1\2\u0248\u0249\5")
        buf.write("\22\n\2\u0249\u024a\5z>\2\u024a\u024b\5\20\t\2\u024b\u0254")
        buf.write("\3\2\2\2\u024c\u024d\f\3\2\2\u024d\u024e\78\2\2\u024e")
        buf.write("\u024f\5\22\n\2\u024f\u0250\5z>\2\u0250\u0251\5\20\t\2")
        buf.write("\u0251\u0253\3\2\2\2\u0252\u024c\3\2\2\2\u0253\u0256\3")
        buf.write("\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255o")
        buf.write("\3\2\2\2\u0256\u0254\3\2\2\2\u0257\u0258\7\66\2\2\u0258")
        buf.write("\u0259\5r:\2\u0259\u025a\7\67\2\2\u025aq\3\2\2\2\u025b")
        buf.write("\u025c\b:\1\2\u025c\u025d\7\30\2\2\u025d\u025e\5z>\2\u025e")
        buf.write("\u025f\5\20\t\2\u025f\u0260\79\2\2\u0260\u0269\3\2\2\2")
        buf.write("\u0261\u0262\f\3\2\2\u0262\u0263\7\30\2\2\u0263\u0264")
        buf.write("\5z>\2\u0264\u0265\5\20\t\2\u0265\u0266\79\2\2\u0266\u0268")
        buf.write("\3\2\2\2\u0267\u0261\3\2\2\2\u0268\u026b\3\2\2\2\u0269")
        buf.write("\u0267\3\2\2\2\u0269\u026a\3\2\2\2\u026as\3\2\2\2\u026b")
        buf.write("\u0269\3\2\2\2\u026c\u0274\5|?\2\u026d\u0274\5\u0082B")
        buf.write("\2\u026e\u0274\7\3\2\2\u026f\u0274\7\31\2\2\u0270\u0274")
        buf.write("\7\36\2\2\u0271\u0274\7>\2\2\u0272\u0274\7\27\2\2\u0273")
        buf.write("\u026c\3\2\2\2\u0273\u026d\3\2\2\2\u0273\u026e\3\2\2\2")
        buf.write("\u0273\u026f\3\2\2\2\u0273\u0270\3\2\2\2\u0273\u0271\3")
        buf.write("\2\2\2\u0273\u0272\3\2\2\2\u0274u\3\2\2\2\u0275\u027e")
        buf.write("\5\u0082B\2\u0276\u027e\7\3\2\2\u0277\u027e\7\31\2\2\u0278")
        buf.write("\u027e\7\36\2\2\u0279\u027e\7>\2\2\u027a\u027e\7\30\2")
        buf.write("\2\u027b\u027e\7\27\2\2\u027c\u027e\5\u0080A\2\u027d\u0275")
        buf.write("\3\2\2\2\u027d\u0276\3\2\2\2\u027d\u0277\3\2\2\2\u027d")
        buf.write("\u0278\3\2\2\2\u027d\u0279\3\2\2\2\u027d\u027a\3\2\2\2")
        buf.write("\u027d\u027b\3\2\2\2\u027d\u027c\3\2\2\2\u027ew\3\2\2")
        buf.write("\2\u027f\u0280\7\64\2\2\u0280\u0281\7\30\2\2\u0281\u0282")
        buf.write("\7\65\2\2\u0282\u0288\5z>\2\u0283\u0284\7\64\2\2\u0284")
        buf.write("\u0285\7\31\2\2\u0285\u0286\7\65\2\2\u0286\u0288\5z>\2")
        buf.write("\u0287\u027f\3\2\2\2\u0287\u0283\3\2\2\2\u0288y\3\2\2")
        buf.write("\2\u0289\u028c\5x=\2\u028a\u028c\3\2\2\2\u028b\u0289\3")
        buf.write("\2\2\2\u028b\u028a\3\2\2\2\u028c{\3\2\2\2\u028d\u028e")
        buf.write("\5x=\2\u028e\u028f\5\20\t\2\u028f\u0290\5\u0080A\2\u0290")
        buf.write("}\3\2\2\2\u0291\u0297\5v<\2\u0292\u0293\5v<\2\u0293\u0294")
        buf.write("\78\2\2\u0294\u0295\5~@\2\u0295\u0297\3\2\2\2\u0296\u0291")
        buf.write("\3\2\2\2\u0296\u0292\3\2\2\2\u0297\177\3\2\2\2\u0298\u0299")
        buf.write("\7\66\2\2\u0299\u029a\5~@\2\u029a\u029b\7\67\2\2\u029b")
        buf.write("\u0081\3\2\2\2\u029c\u029d\7\30\2\2\u029d\u029e\7\66\2")
        buf.write("\2\u029e\u029f\5\u0084C\2\u029f\u02a0\7\67\2\2\u02a0\u02a5")
        buf.write("\3\2\2\2\u02a1\u02a2\7\30\2\2\u02a2\u02a3\7\66\2\2\u02a3")
        buf.write("\u02a5\7\67\2\2\u02a4\u029c\3\2\2\2\u02a4\u02a1\3\2\2")
        buf.write("\2\u02a5\u0083\3\2\2\2\u02a6\u02a7\bC\1\2\u02a7\u02a8")
        buf.write("\7\30\2\2\u02a8\u02a9\7:\2\2\u02a9\u02aa\5@!\2\u02aa\u02b2")
        buf.write("\3\2\2\2\u02ab\u02ac\f\3\2\2\u02ac\u02ad\78\2\2\u02ad")
        buf.write("\u02ae\7\30\2\2\u02ae\u02af\7:\2\2\u02af\u02b1\5@!\2\u02b0")
        buf.write("\u02ab\3\2\2\2\u02b1\u02b4\3\2\2\2\u02b2\u02b0\3\2\2\2")
        buf.write("\u02b2\u02b3\3\2\2\2\u02b3\u0085\3\2\2\2\u02b4\u02b2\3")
        buf.write("\2\2\2\60\u008d\u0092\u0097\u00ab\u00bb\u00cd\u00d8\u00de")
        buf.write("\u00e6\u00ff\u010a\u0118\u0120\u0125\u014b\u015d\u0166")
        buf.write("\u0170\u017f\u018c\u0197\u01a3\u01b1\u01b3\u01c2\u01c4")
        buf.write("\u01cc\u01d2\u01dd\u01df\u01e9\u0201\u020f\u021a\u021e")
        buf.write("\u0240\u0245\u0254\u0269\u0273\u027d\u0287\u028b\u0296")
        buf.write("\u02a4\u02b2")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "'else'", "'true'", 
                     "'false'", "'for'", "'range'", "'break'", "'continue'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'var'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'nil'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'=='", "'!='", "'>'", "'<'", 
                     "'>='", "'<='", "'!'", "'&&'", "'||'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "';'", "':'", "'.'", 
                     "':='", "'='", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "BOOLITERAL", "IF", "ELSE", "TRUE", "FALSE", 
                      "FOR", "RANGE", "BREAK", "CONTINUE", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "VAR", "STRING", "INTTYPE", 
                      "FLOAT", "BOOLEAN", "CONST", "NIL", "ID", "INT", "DECINT", 
                      "BININT", "OCTINT", "HEXINT", "REAL", "ADD", "MINUS", 
                      "MUL", "DIV", "MOD", "ADDAS", "MiNUSAS", "MULAS", 
                      "DIVAS", "MODAS", "EQUAL", "NEQUAL", "BIG", "SMALL", 
                      "EBIG", "ESMALL", "NOT", "AND", "OR", "LB", "RB", 
                      "LS", "RS", "LC", "RC", "COMMA", "SEMI", "COLON", 
                      "DOT", "AS1", "AS2", "STRINGLIT", "NL", "WS", "COMMENT1", 
                      "COMMENT2", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_program_tail = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_var = 4
    RULE_vararray = 5
    RULE_const = 6
    RULE_alltype = 7
    RULE_list_id = 8
    RULE_funcdecl = 9
    RULE_functype = 10
    RULE_param = 11
    RULE_funcbody = 12
    RULE_funcstruct = 13
    RULE_list_stmts = 14
    RULE_stmts = 15
    RULE_continue_stmt = 16
    RULE_break_stmt = 17
    RULE_return_stmt = 18
    RULE_call_stmts = 19
    RULE_for_stmt = 20
    RULE_for_condition = 21
    RULE_for_update = 22
    RULE_for_array = 23
    RULE_assign_stmts = 24
    RULE_lhs_assign = 25
    RULE_assign = 26
    RULE_if_stms = 27
    RULE_ifelse = 28
    RULE_condition = 29
    RULE_expr_list = 30
    RULE_expr = 31
    RULE_or_expr = 32
    RULE_and_expr = 33
    RULE_logic_expr = 34
    RULE_compare = 35
    RULE_add_expr = 36
    RULE_mul_expr = 37
    RULE_neg_expr = 38
    RULE_element_expr = 39
    RULE_struct_expr = 40
    RULE_factor_expr = 41
    RULE_access_struct = 42
    RULE_method_element = 43
    RULE_array_element = 44
    RULE_access_field = 45
    RULE_method_op = 46
    RULE_index_op = 47
    RULE_funccall = 48
    RULE_typedecl = 49
    RULE_type_stuct = 50
    RULE_type_inter = 51
    RULE_body_inter = 52
    RULE_parammethod_op = 53
    RULE_parammethod = 54
    RULE_body_type = 55
    RULE_body_body_type = 56
    RULE_literal = 57
    RULE_literal_array = 58
    RULE_space_array = 59
    RULE_space_array_op = 60
    RULE_array = 61
    RULE_array_nested = 62
    RULE_array_list = 63
    RULE_struct_literal = 64
    RULE_struct_param = 65

    ruleNames =  [ "program", "program_tail", "decl", "vardecl", "var", 
                   "vararray", "const", "alltype", "list_id", "funcdecl", 
                   "functype", "param", "funcbody", "funcstruct", "list_stmts", 
                   "stmts", "continue_stmt", "break_stmt", "return_stmt", 
                   "call_stmts", "for_stmt", "for_condition", "for_update", 
                   "for_array", "assign_stmts", "lhs_assign", "assign", 
                   "if_stms", "ifelse", "condition", "expr_list", "expr", 
                   "or_expr", "and_expr", "logic_expr", "compare", "add_expr", 
                   "mul_expr", "neg_expr", "element_expr", "struct_expr", 
                   "factor_expr", "access_struct", "method_element", "array_element", 
                   "access_field", "method_op", "index_op", "funccall", 
                   "typedecl", "type_stuct", "type_inter", "body_inter", 
                   "parammethod_op", "parammethod", "body_type", "body_body_type", 
                   "literal", "literal_array", "space_array", "space_array_op", 
                   "array", "array_nested", "array_list", "struct_literal", 
                   "struct_param" ]

    EOF = Token.EOF
    BOOLITERAL=1
    IF=2
    ELSE=3
    TRUE=4
    FALSE=5
    FOR=6
    RANGE=7
    BREAK=8
    CONTINUE=9
    RETURN=10
    FUNC=11
    TYPE=12
    STRUCT=13
    INTERFACE=14
    VAR=15
    STRING=16
    INTTYPE=17
    FLOAT=18
    BOOLEAN=19
    CONST=20
    NIL=21
    ID=22
    INT=23
    DECINT=24
    BININT=25
    OCTINT=26
    HEXINT=27
    REAL=28
    ADD=29
    MINUS=30
    MUL=31
    DIV=32
    MOD=33
    ADDAS=34
    MiNUSAS=35
    MULAS=36
    DIVAS=37
    MODAS=38
    EQUAL=39
    NEQUAL=40
    BIG=41
    SMALL=42
    EBIG=43
    ESMALL=44
    NOT=45
    AND=46
    OR=47
    LB=48
    RB=49
    LS=50
    RS=51
    LC=52
    RC=53
    COMMA=54
    SEMI=55
    COLON=56
    DOT=57
    AS1=58
    AS2=59
    STRINGLIT=60
    NL=61
    WS=62
    COMMENT1=63
    COMMENT2=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66
    ERROR_CHAR=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def program_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Program_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.decl()
            self.state = 133
            self.program_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def program_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Program_tailContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_tail" ):
                return visitor.visitProgram_tail(self)
            else:
                return visitor.visitChildren(self)




    def program_tail(self):

        localctx = MiniGoParser.Program_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_tail)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.VAR, MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.decl()
                self.state = 136
                self.program_tail()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(MiniGoParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.funcdecl()
                pass
            elif token in [MiniGoParser.VAR, MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.vardecl()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.typedecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vararray(self):
            return self.getTypedRuleContext(MiniGoParser.VararrayContext,0)


        def var(self):
            return self.getTypedRuleContext(MiniGoParser.VarContext,0)


        def const(self):
            return self.getTypedRuleContext(MiniGoParser.ConstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.vararray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.const()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def alltype(self):
            return self.getTypedRuleContext(MiniGoParser.AlltypeContext,0)


        def AS2(self):
            return self.getToken(MiniGoParser.AS2, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MiniGoParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(MiniGoParser.VAR)
                self.state = 152
                self.match(MiniGoParser.ID)
                self.state = 153
                self.alltype()
                self.state = 154
                self.match(MiniGoParser.AS2)
                self.state = 155
                self.expr()
                self.state = 156
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(MiniGoParser.VAR)
                self.state = 159
                self.match(MiniGoParser.ID)
                self.state = 160
                self.alltype()
                self.state = 161
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(MiniGoParser.VAR)
                self.state = 164
                self.match(MiniGoParser.ID)
                self.state = 165
                self.match(MiniGoParser.AS2)
                self.state = 166
                self.expr()
                self.state = 167
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VararrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def space_array(self):
            return self.getTypedRuleContext(MiniGoParser.Space_arrayContext,0)


        def alltype(self):
            return self.getTypedRuleContext(MiniGoParser.AlltypeContext,0)


        def AS2(self):
            return self.getToken(MiniGoParser.AS2, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vararray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVararray" ):
                return visitor.visitVararray(self)
            else:
                return visitor.visitChildren(self)




    def vararray(self):

        localctx = MiniGoParser.VararrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vararray)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(MiniGoParser.VAR)
                self.state = 172
                self.match(MiniGoParser.ID)
                self.state = 173
                self.space_array()
                self.state = 174
                self.alltype()
                self.state = 175
                self.match(MiniGoParser.AS2)
                self.state = 176
                self.expr()
                self.state = 177
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(MiniGoParser.VAR)
                self.state = 180
                self.match(MiniGoParser.ID)
                self.state = 181
                self.space_array()
                self.state = 182
                self.alltype()
                self.state = 183
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def AS2(self):
            return self.getToken(MiniGoParser.AS2, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = MiniGoParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MiniGoParser.CONST)
            self.state = 188
            self.match(MiniGoParser.ID)
            self.state = 189
            self.match(MiniGoParser.AS2)
            self.state = 190
            self.expr()
            self.state = 191
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlltypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def INTTYPE(self):
            return self.getToken(MiniGoParser.INTTYPE, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_alltype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlltype" ):
                return visitor.visitAlltype(self)
            else:
                return visitor.visitChildren(self)




    def alltype(self):

        localctx = MiniGoParser.AlltypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_alltype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INTTYPE) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def list_id(self):
            return self.getTypedRuleContext(MiniGoParser.List_idContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_id" ):
                return visitor.visitList_id(self)
            else:
                return visitor.visitChildren(self)



    def list_id(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.List_idContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_list_id, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.List_idContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_list_id)
                    self.state = 198
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 199
                    self.match(MiniGoParser.COMMA)
                    self.state = 200
                    self.match(MiniGoParser.ID) 
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def functype(self):
            return self.getTypedRuleContext(MiniGoParser.FunctypeContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncbodyContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def funcstruct(self):
            return self.getTypedRuleContext(MiniGoParser.FuncstructContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(MiniGoParser.FUNC)
                self.state = 207
                self.match(MiniGoParser.ID)
                self.state = 208
                self.param()
                self.state = 209
                self.functype()
                self.state = 210
                self.funcbody()
                self.state = 211
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.funcstruct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_array_op(self):
            return self.getTypedRuleContext(MiniGoParser.Space_array_opContext,0)


        def alltype(self):
            return self.getTypedRuleContext(MiniGoParser.AlltypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctype" ):
                return visitor.visitFunctype(self)
            else:
                return visitor.visitChildren(self)




    def functype(self):

        localctx = MiniGoParser.FunctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functype)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INTTYPE, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID, MiniGoParser.LS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.space_array_op()
                self.state = 217
                self.alltype()
                pass
            elif token in [MiniGoParser.LC, MiniGoParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def parammethod(self):
            return self.getTypedRuleContext(MiniGoParser.ParammethodContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(MiniGoParser.LB)
                self.state = 223
                self.parammethod(0)
                self.state = 224
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MiniGoParser.LB)
                self.state = 227
                self.match(MiniGoParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(MiniGoParser.List_stmtsContext,0)


        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncbody" ):
                return visitor.visitFuncbody(self)
            else:
                return visitor.visitChildren(self)




    def funcbody(self):

        localctx = MiniGoParser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(MiniGoParser.LC)
            self.state = 231
            self.list_stmts(0)
            self.state = 232
            self.match(MiniGoParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncstructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def space_array_op(self):
            return self.getTypedRuleContext(MiniGoParser.Space_array_opContext,0)


        def alltype(self):
            return self.getTypedRuleContext(MiniGoParser.AlltypeContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def functype(self):
            return self.getTypedRuleContext(MiniGoParser.FunctypeContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncbodyContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcstruct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncstruct" ):
                return visitor.visitFuncstruct(self)
            else:
                return visitor.visitChildren(self)




    def funcstruct(self):

        localctx = MiniGoParser.FuncstructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcstruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.FUNC)
            self.state = 235
            self.match(MiniGoParser.LB)
            self.state = 236
            self.match(MiniGoParser.ID)
            self.state = 237
            self.space_array_op()
            self.state = 238
            self.alltype()
            self.state = 239
            self.match(MiniGoParser.RB)
            self.state = 240
            self.match(MiniGoParser.ID)
            self.state = 241
            self.param()
            self.state = 242
            self.functype()
            self.state = 243
            self.funcbody()
            self.state = 244
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmts(self):
            return self.getTypedRuleContext(MiniGoParser.StmtsContext,0)


        def list_stmts(self):
            return self.getTypedRuleContext(MiniGoParser.List_stmtsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmts" ):
                return visitor.visitList_stmts(self)
            else:
                return visitor.visitChildren(self)



    def list_stmts(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.List_stmtsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_list_stmts, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.stmts()
            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.List_stmtsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_list_stmts)
                    self.state = 249
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 250
                    self.stmts() 
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmts(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtsContext,0)


        def if_stms(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmsContext,0)


        def call_stmts(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtsContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = MiniGoParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmts)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.assign_stmts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.if_stms()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.call_stmts()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.continue_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.vardecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 263
                self.for_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MiniGoParser.CONTINUE)
            self.state = 267
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(MiniGoParser.BREAK)
            self.state = 270
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_stmt)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(MiniGoParser.RETURN)
                self.state = 273
                self.expr()
                self.state = 274
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(MiniGoParser.RETURN)
                self.state = 277
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_element(self):
            return self.getTypedRuleContext(MiniGoParser.Method_elementContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmts" ):
                return visitor.visitCall_stmts(self)
            else:
                return visitor.visitChildren(self)




    def call_stmts(self):

        localctx = MiniGoParser.Call_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_call_stmts)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.method_element()
                self.state = 281
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.funccall()
                self.state = 284
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_condition(self):
            return self.getTypedRuleContext(MiniGoParser.For_conditionContext,0)


        def for_update(self):
            return self.getTypedRuleContext(MiniGoParser.For_updateContext,0)


        def for_array(self):
            return self.getTypedRuleContext(MiniGoParser.For_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_for_stmt)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.for_condition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.for_update()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.for_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncbodyContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = MiniGoParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.FOR)
            self.state = 294
            self.expr()
            self.state = 295
            self.funcbody()
            self.state = 296
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_updateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def funcbody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_update" ):
                return visitor.visitFor_update(self)
            else:
                return visitor.visitChildren(self)




    def for_update(self):

        localctx = MiniGoParser.For_updateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(MiniGoParser.FOR)
            self.state = 299
            self.match(MiniGoParser.ID)
            self.state = 300
            self.assign()
            self.state = 301
            self.expr()
            self.state = 302
            self.match(MiniGoParser.SEMI)
            self.state = 303
            self.expr()
            self.state = 304
            self.match(MiniGoParser.SEMI)
            self.state = 305
            self.match(MiniGoParser.ID)
            self.state = 306
            self.assign()
            self.state = 307
            self.expr()
            self.state = 308
            self.funcbody()
            self.state = 309
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def AS1(self):
            return self.getToken(MiniGoParser.AS1, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncbodyContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_array" ):
                return visitor.visitFor_array(self)
            else:
                return visitor.visitChildren(self)




    def for_array(self):

        localctx = MiniGoParser.For_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(MiniGoParser.FOR)
            self.state = 312
            self.match(MiniGoParser.ID)
            self.state = 313
            self.match(MiniGoParser.COMMA)
            self.state = 314
            self.match(MiniGoParser.ID)
            self.state = 315
            self.match(MiniGoParser.AS1)
            self.state = 316
            self.match(MiniGoParser.RANGE)
            self.state = 317
            self.expr()
            self.state = 318
            self.funcbody()
            self.state = 319
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_assignContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmts" ):
                return visitor.visitAssign_stmts(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmts(self):

        localctx = MiniGoParser.Assign_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assign_stmts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.lhs_assign()
            self.state = 322
            self.assign()
            self.state = 323
            self.expr()
            self.state = 324
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def access_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Access_structContext,0)


        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_assign" ):
                return visitor.visitLhs_assign(self)
            else:
                return visitor.visitChildren(self)




    def lhs_assign(self):

        localctx = MiniGoParser.Lhs_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lhs_assign)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.access_struct()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS1(self):
            return self.getToken(MiniGoParser.AS1, 0)

        def ADDAS(self):
            return self.getToken(MiniGoParser.ADDAS, 0)

        def MiNUSAS(self):
            return self.getToken(MiniGoParser.MiNUSAS, 0)

        def MULAS(self):
            return self.getToken(MiniGoParser.MULAS, 0)

        def DIVAS(self):
            return self.getToken(MiniGoParser.DIVAS, 0)

        def MODAS(self):
            return self.getToken(MiniGoParser.MODAS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADDAS) | (1 << MiniGoParser.MiNUSAS) | (1 << MiniGoParser.MULAS) | (1 << MiniGoParser.DIVAS) | (1 << MiniGoParser.MODAS) | (1 << MiniGoParser.AS1))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def funcbody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncbodyContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncbodyContext,i)


        def ifelse(self):
            return self.getTypedRuleContext(MiniGoParser.IfelseContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stms

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stms" ):
                return visitor.visitIf_stms(self)
            else:
                return visitor.visitChildren(self)




    def if_stms(self):

        localctx = MiniGoParser.If_stmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stms)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(MiniGoParser.IF)
                self.state = 334
                self.condition()
                self.state = 335
                self.funcbody()
                self.state = 336
                self.ifelse(0)
                self.state = 337
                self.match(MiniGoParser.ELSE)
                self.state = 338
                self.funcbody()
                self.state = 339
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(MiniGoParser.IF)
                self.state = 342
                self.condition()
                self.state = 343
                self.funcbody()
                self.state = 344
                self.ifelse(0)
                self.state = 345
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncbodyContext,0)


        def ifelse(self):
            return self.getTypedRuleContext(MiniGoParser.IfelseContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)



    def ifelse(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.IfelseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_ifelse, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 350
                self.match(MiniGoParser.ELSE)
                self.state = 351
                self.match(MiniGoParser.IF)
                self.state = 352
                self.condition()
                self.state = 353
                self.funcbody()
                pass

            elif la_ == 2:
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.IfelseContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_ifelse)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    self.match(MiniGoParser.ELSE)
                    self.state = 360
                    self.match(MiniGoParser.IF)
                    self.state = 361
                    self.condition()
                    self.state = 362
                    self.funcbody() 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(MiniGoParser.LB)
            self.state = 370
            self.expr()
            self.state = 371
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)



    def expr_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_list)
                    self.state = 376
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 377
                    self.match(MiniGoParser.COMMA)
                    self.state = 378
                    self.expr() 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Or_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniGoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.or_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.And_exprContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Or_exprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_or_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_expr" ):
                return visitor.visitOr_expr(self)
            else:
                return visitor.visitChildren(self)



    def or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    self.match(MiniGoParser.OR)
                    self.state = 391
                    self.and_expr(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logic_exprContext,0)


        def and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.And_exprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_and_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expr" ):
                return visitor.visitAnd_expr(self)
            else:
                return visitor.visitChildren(self)



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.logic_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    self.match(MiniGoParser.AND)
                    self.state = 402
                    self.logic_expr(0) 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Add_exprContext,0)


        def logic_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logic_exprContext,0)


        def compare(self):
            return self.getTypedRuleContext(MiniGoParser.CompareContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_logic_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_expr" ):
                return visitor.visitLogic_expr(self)
            else:
                return visitor.visitChildren(self)



    def logic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Logic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logic_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    self.compare()
                    self.state = 413
                    self.add_expr(0) 
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(MiniGoParser.NEQUAL, 0)

        def BIG(self):
            return self.getToken(MiniGoParser.BIG, 0)

        def SMALL(self):
            return self.getToken(MiniGoParser.SMALL, 0)

        def EBIG(self):
            return self.getToken(MiniGoParser.EBIG, 0)

        def ESMALL(self):
            return self.getToken(MiniGoParser.ESMALL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)




    def compare(self):

        localctx = MiniGoParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NEQUAL) | (1 << MiniGoParser.BIG) | (1 << MiniGoParser.SMALL) | (1 << MiniGoParser.EBIG) | (1 << MiniGoParser.ESMALL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Add_exprContext,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_add_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 431
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Add_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                        self.state = 425
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 426
                        self.match(MiniGoParser.ADD)
                        self.state = 427
                        self.mul_expr(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Add_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                        self.state = 428
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 429
                        self.match(MiniGoParser.MINUS)
                        self.state = 430
                        self.mul_expr(0)
                        pass

             
                self.state = 435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def neg_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Neg_exprContext,0)


        def mul_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_exprContext,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)



    def mul_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Mul_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_mul_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.neg_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 448
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Mul_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                        self.state = 439
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 440
                        self.match(MiniGoParser.MUL)
                        self.state = 441
                        self.neg_expr()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Mul_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                        self.state = 442
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 443
                        self.match(MiniGoParser.DIV)
                        self.state = 444
                        self.neg_expr()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Mul_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                        self.state = 445
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 446
                        self.match(MiniGoParser.MOD)
                        self.state = 447
                        self.neg_expr()
                        pass

             
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Neg_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def neg_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Neg_exprContext,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def element_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Element_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_neg_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg_expr" ):
                return visitor.visitNeg_expr(self)
            else:
                return visitor.visitChildren(self)




    def neg_expr(self):

        localctx = MiniGoParser.Neg_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_neg_expr)
        try:
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(MiniGoParser.MINUS)
                self.state = 454
                self.neg_expr()
                pass
            elif token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.match(MiniGoParser.NOT)
                self.state = 456
                self.neg_expr()
                pass
            elif token in [MiniGoParser.BOOLITERAL, MiniGoParser.NIL, MiniGoParser.ID, MiniGoParser.INT, MiniGoParser.REAL, MiniGoParser.LB, MiniGoParser.LS, MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.element_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_element(self):
            return self.getTypedRuleContext(MiniGoParser.Method_elementContext,0)


        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def access_struct(self):
            return self.getTypedRuleContext(MiniGoParser.Access_structContext,0)


        def factor_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Factor_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




    def element_expr(self):

        localctx = MiniGoParser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_element_expr)
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.method_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.array_element()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.access_struct()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 463
                self.factor_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Factor_exprContext,0)


        def struct_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_exprContext,0)


        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def method_op(self):
            return self.getTypedRuleContext(MiniGoParser.Method_opContext,0)


        def index_op(self):
            return self.getTypedRuleContext(MiniGoParser.Index_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_expr" ):
                return visitor.visitStruct_expr(self)
            else:
                return visitor.visitChildren(self)



    def struct_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Struct_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_struct_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.factor_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 477
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 475
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Struct_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_expr)
                        self.state = 469
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 470
                        self.access_field()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Struct_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_expr)
                        self.state = 471
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 472
                        self.method_op()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Struct_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_expr)
                        self.state = 473
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 474
                        self.index_op(0)
                        pass

             
                self.state = 479
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Factor_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_factor_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_expr" ):
                return visitor.visitFactor_expr(self)
            else:
                return visitor.visitChildren(self)




    def factor_expr(self):

        localctx = MiniGoParser.Factor_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_factor_expr)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(MiniGoParser.LB)
                self.state = 481
                self.expr()
                self.state = 482
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 485
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 486
                self.funccall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_structContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_exprContext,0)


        def access_field(self):
            return self.getTypedRuleContext(MiniGoParser.Access_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_access_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_struct" ):
                return visitor.visitAccess_struct(self)
            else:
                return visitor.visitChildren(self)




    def access_struct(self):

        localctx = MiniGoParser.Access_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_access_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.struct_expr(0)
            self.state = 490
            self.access_field()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_exprContext,0)


        def method_op(self):
            return self.getTypedRuleContext(MiniGoParser.Method_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_element" ):
                return visitor.visitMethod_element(self)
            else:
                return visitor.visitChildren(self)




    def method_element(self):

        localctx = MiniGoParser.Method_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_method_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.struct_expr(0)
            self.state = 493
            self.method_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_exprContext,0)


        def index_op(self):
            return self.getTypedRuleContext(MiniGoParser.Index_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.struct_expr(0)
            self.state = 496
            self.index_op(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_access_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_field" ):
                return visitor.visitAccess_field(self)
            else:
                return visitor.visitChildren(self)




    def access_field(self):

        localctx = MiniGoParser.Access_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_access_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MiniGoParser.DOT)
            self.state = 499
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_op" ):
                return visitor.visitMethod_op(self)
            else:
                return visitor.visitChildren(self)




    def method_op(self):

        localctx = MiniGoParser.Method_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_method_op)
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(MiniGoParser.DOT)
                self.state = 502
                self.match(MiniGoParser.ID)
                self.state = 503
                self.match(MiniGoParser.LB)
                self.state = 504
                self.expr_list(0)
                self.state = 505
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.match(MiniGoParser.DOT)
                self.state = 508
                self.match(MiniGoParser.ID)
                self.state = 509
                self.match(MiniGoParser.LB)
                self.state = 510
                self.match(MiniGoParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(MiniGoParser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RS(self):
            return self.getToken(MiniGoParser.RS, 0)

        def index_op(self):
            return self.getTypedRuleContext(MiniGoParser.Index_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)



    def index_op(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Index_opContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_index_op, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(MiniGoParser.LS)
            self.state = 515
            self.expr()
            self.state = 516
            self.match(MiniGoParser.RS)
            self._ctx.stop = self._input.LT(-1)
            self.state = 525
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Index_opContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_op)
                    self.state = 518
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 519
                    self.match(MiniGoParser.LS)
                    self.state = 520
                    self.expr()
                    self.state = 521
                    self.match(MiniGoParser.RS) 
                self.state = 527
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MiniGoParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_funccall)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.match(MiniGoParser.ID)
                self.state = 529
                self.match(MiniGoParser.LB)
                self.state = 530
                self.expr_list(0)
                self.state = 531
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(MiniGoParser.ID)
                self.state = 534
                self.match(MiniGoParser.LB)
                self.state = 535
                self.match(MiniGoParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_stuct(self):
            return self.getTypedRuleContext(MiniGoParser.Type_stuctContext,0)


        def type_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Type_interContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = MiniGoParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_typedecl)
        try:
            self.state = 540
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.type_stuct()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.type_inter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_stuctContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def body_type(self):
            return self.getTypedRuleContext(MiniGoParser.Body_typeContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_stuct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_stuct" ):
                return visitor.visitType_stuct(self)
            else:
                return visitor.visitChildren(self)




    def type_stuct(self):

        localctx = MiniGoParser.Type_stuctContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_type_stuct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(MiniGoParser.TYPE)
            self.state = 543
            self.match(MiniGoParser.ID)
            self.state = 544
            self.match(MiniGoParser.STRUCT)
            self.state = 545
            self.body_type()
            self.state = 546
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_interContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def body_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Body_interContext,0)


        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_type_inter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_inter" ):
                return visitor.visitType_inter(self)
            else:
                return visitor.visitChildren(self)




    def type_inter(self):

        localctx = MiniGoParser.Type_interContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_type_inter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(MiniGoParser.TYPE)
            self.state = 549
            self.match(MiniGoParser.ID)
            self.state = 550
            self.match(MiniGoParser.INTERFACE)
            self.state = 551
            self.match(MiniGoParser.LC)
            self.state = 552
            self.body_inter(0)
            self.state = 553
            self.match(MiniGoParser.RC)
            self.state = 554
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_interContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def parammethod_op(self):
            return self.getTypedRuleContext(MiniGoParser.Parammethod_opContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def functype(self):
            return self.getTypedRuleContext(MiniGoParser.FunctypeContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def body_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Body_interContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_body_inter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_inter" ):
                return visitor.visitBody_inter(self)
            else:
                return visitor.visitChildren(self)



    def body_inter(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Body_interContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_body_inter, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(MiniGoParser.ID)
            self.state = 558
            self.match(MiniGoParser.LB)
            self.state = 559
            self.parammethod_op()
            self.state = 560
            self.match(MiniGoParser.RB)
            self.state = 561
            self.functype()
            self.state = 562
            self.match(MiniGoParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 574
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Body_interContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_body_inter)
                    self.state = 564
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 565
                    self.match(MiniGoParser.ID)
                    self.state = 566
                    self.match(MiniGoParser.LB)
                    self.state = 567
                    self.parammethod_op()
                    self.state = 568
                    self.match(MiniGoParser.RB)
                    self.state = 569
                    self.functype()
                    self.state = 570
                    self.match(MiniGoParser.SEMI) 
                self.state = 576
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Parammethod_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parammethod(self):
            return self.getTypedRuleContext(MiniGoParser.ParammethodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parammethod_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParammethod_op" ):
                return visitor.visitParammethod_op(self)
            else:
                return visitor.visitChildren(self)




    def parammethod_op(self):

        localctx = MiniGoParser.Parammethod_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_parammethod_op)
        try:
            self.state = 579
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.parammethod(0)
                pass
            elif token in [MiniGoParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParammethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_id(self):
            return self.getTypedRuleContext(MiniGoParser.List_idContext,0)


        def space_array_op(self):
            return self.getTypedRuleContext(MiniGoParser.Space_array_opContext,0)


        def alltype(self):
            return self.getTypedRuleContext(MiniGoParser.AlltypeContext,0)


        def parammethod(self):
            return self.getTypedRuleContext(MiniGoParser.ParammethodContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_parammethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParammethod" ):
                return visitor.visitParammethod(self)
            else:
                return visitor.visitChildren(self)



    def parammethod(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ParammethodContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_parammethod, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.list_id(0)
            self.state = 583
            self.space_array_op()
            self.state = 584
            self.alltype()
            self._ctx.stop = self._input.LT(-1)
            self.state = 594
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ParammethodContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parammethod)
                    self.state = 586
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 587
                    self.match(MiniGoParser.COMMA)
                    self.state = 588
                    self.list_id(0)
                    self.state = 589
                    self.space_array_op()
                    self.state = 590
                    self.alltype() 
                self.state = 596
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Body_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def body_body_type(self):
            return self.getTypedRuleContext(MiniGoParser.Body_body_typeContext,0)


        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_body_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_type" ):
                return visitor.visitBody_type(self)
            else:
                return visitor.visitChildren(self)




    def body_type(self):

        localctx = MiniGoParser.Body_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_body_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(MiniGoParser.LC)
            self.state = 598
            self.body_body_type(0)
            self.state = 599
            self.match(MiniGoParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_body_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def space_array_op(self):
            return self.getTypedRuleContext(MiniGoParser.Space_array_opContext,0)


        def alltype(self):
            return self.getTypedRuleContext(MiniGoParser.AlltypeContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def body_body_type(self):
            return self.getTypedRuleContext(MiniGoParser.Body_body_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_body_body_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_body_type" ):
                return visitor.visitBody_body_type(self)
            else:
                return visitor.visitChildren(self)



    def body_body_type(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Body_body_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_body_body_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(MiniGoParser.ID)
            self.state = 603
            self.space_array_op()
            self.state = 604
            self.alltype()
            self.state = 605
            self.match(MiniGoParser.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 615
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Body_body_typeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_body_body_type)
                    self.state = 607
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 608
                    self.match(MiniGoParser.ID)
                    self.state = 609
                    self.space_array_op()
                    self.state = 610
                    self.alltype()
                    self.state = 611
                    self.match(MiniGoParser.SEMI) 
                self.state = 617
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def BOOLITERAL(self):
            return self.getToken(MiniGoParser.BOOLITERAL, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def REAL(self):
            return self.getToken(MiniGoParser.REAL, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_literal)
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                self.array()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 619
                self.struct_literal()
                pass
            elif token in [MiniGoParser.BOOLITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 620
                self.match(MiniGoParser.BOOLITERAL)
                pass
            elif token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 621
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.REAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 622
                self.match(MiniGoParser.REAL)
                pass
            elif token in [MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 623
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 624
                self.match(MiniGoParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def BOOLITERAL(self):
            return self.getToken(MiniGoParser.BOOLITERAL, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def REAL(self):
            return self.getToken(MiniGoParser.REAL, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def array_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_array" ):
                return visitor.visitLiteral_array(self)
            else:
                return visitor.visitChildren(self)




    def literal_array(self):

        localctx = MiniGoParser.Literal_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_literal_array)
        try:
            self.state = 635
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 627
                self.struct_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 628
                self.match(MiniGoParser.BOOLITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 629
                self.match(MiniGoParser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 630
                self.match(MiniGoParser.REAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 631
                self.match(MiniGoParser.STRINGLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 632
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 633
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 634
                self.array_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Space_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(MiniGoParser.LS, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def RS(self):
            return self.getToken(MiniGoParser.RS, 0)

        def space_array_op(self):
            return self.getTypedRuleContext(MiniGoParser.Space_array_opContext,0)


        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_space_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpace_array" ):
                return visitor.visitSpace_array(self)
            else:
                return visitor.visitChildren(self)




    def space_array(self):

        localctx = MiniGoParser.Space_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_space_array)
        try:
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 637
                self.match(MiniGoParser.LS)
                self.state = 638
                self.match(MiniGoParser.ID)
                self.state = 639
                self.match(MiniGoParser.RS)
                self.state = 640
                self.space_array_op()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 641
                self.match(MiniGoParser.LS)
                self.state = 642
                self.match(MiniGoParser.INT)
                self.state = 643
                self.match(MiniGoParser.RS)
                self.state = 644
                self.space_array_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Space_array_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_array(self):
            return self.getTypedRuleContext(MiniGoParser.Space_arrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_space_array_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpace_array_op" ):
                return visitor.visitSpace_array_op(self)
            else:
                return visitor.visitChildren(self)




    def space_array_op(self):

        localctx = MiniGoParser.Space_array_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_space_array_op)
        try:
            self.state = 649
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 647
                self.space_array()
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INTTYPE, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def space_array(self):
            return self.getTypedRuleContext(MiniGoParser.Space_arrayContext,0)


        def alltype(self):
            return self.getTypedRuleContext(MiniGoParser.AlltypeContext,0)


        def array_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MiniGoParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self.space_array()
            self.state = 652
            self.alltype()
            self.state = 653
            self.array_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_nestedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_array(self):
            return self.getTypedRuleContext(MiniGoParser.Literal_arrayContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_nested(self):
            return self.getTypedRuleContext(MiniGoParser.Array_nestedContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_nested

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_nested" ):
                return visitor.visitArray_nested(self)
            else:
                return visitor.visitChildren(self)




    def array_nested(self):

        localctx = MiniGoParser.Array_nestedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_array_nested)
        try:
            self.state = 660
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 655
                self.literal_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
                self.literal_array()
                self.state = 657
                self.match(MiniGoParser.COMMA)
                self.state = 658
                self.array_nested()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def array_nested(self):
            return self.getTypedRuleContext(MiniGoParser.Array_nestedContext,0)


        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = MiniGoParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 662
            self.match(MiniGoParser.LC)
            self.state = 663
            self.array_nested()
            self.state = 664
            self.match(MiniGoParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LC(self):
            return self.getToken(MiniGoParser.LC, 0)

        def struct_param(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_paramContext,0)


        def RC(self):
            return self.getToken(MiniGoParser.RC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_struct_literal)
        try:
            self.state = 674
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 666
                self.match(MiniGoParser.ID)
                self.state = 667
                self.match(MiniGoParser.LC)
                self.state = 668
                self.struct_param(0)
                self.state = 669
                self.match(MiniGoParser.RC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.match(MiniGoParser.ID)
                self.state = 672
                self.match(MiniGoParser.LC)
                self.state = 673
                self.match(MiniGoParser.RC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def struct_param(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_paramContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_param" ):
                return visitor.visitStruct_param(self)
            else:
                return visitor.visitChildren(self)



    def struct_param(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Struct_paramContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_struct_param, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.match(MiniGoParser.ID)
            self.state = 678
            self.match(MiniGoParser.COLON)
            self.state = 679
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 688
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_paramContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_param)
                    self.state = 681
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 682
                    self.match(MiniGoParser.COMMA)
                    self.state = 683
                    self.match(MiniGoParser.ID)
                    self.state = 684
                    self.match(MiniGoParser.COLON)
                    self.state = 685
                    self.expr() 
                self.state = 690
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.list_id_sempred
        self._predicates[14] = self.list_stmts_sempred
        self._predicates[28] = self.ifelse_sempred
        self._predicates[30] = self.expr_list_sempred
        self._predicates[32] = self.or_expr_sempred
        self._predicates[33] = self.and_expr_sempred
        self._predicates[34] = self.logic_expr_sempred
        self._predicates[36] = self.add_expr_sempred
        self._predicates[37] = self.mul_expr_sempred
        self._predicates[40] = self.struct_expr_sempred
        self._predicates[47] = self.index_op_sempred
        self._predicates[52] = self.body_inter_sempred
        self._predicates[54] = self.parammethod_sempred
        self._predicates[56] = self.body_body_type_sempred
        self._predicates[65] = self.struct_param_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def list_id_sempred(self, localctx:List_idContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def list_stmts_sempred(self, localctx:List_stmtsContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def ifelse_sempred(self, localctx:IfelseContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_list_sempred(self, localctx:Expr_listContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def or_expr_sempred(self, localctx:Or_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def and_expr_sempred(self, localctx:And_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def logic_expr_sempred(self, localctx:Logic_exprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def mul_expr_sempred(self, localctx:Mul_exprContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def struct_expr_sempred(self, localctx:Struct_exprContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def index_op_sempred(self, localctx:Index_opContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 1)
         

    def body_inter_sempred(self, localctx:Body_interContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 1)
         

    def parammethod_sempred(self, localctx:ParammethodContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         

    def body_body_type_sempred(self, localctx:Body_body_typeContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 1)
         

    def struct_param_sempred(self, localctx:Struct_paramContext, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         




