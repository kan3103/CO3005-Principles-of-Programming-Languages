import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    # identifier
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    
    def test_upper_identifier(self):
        """test upper identifier"""
        self.assertTrue(TestLexer.checkLexeme("ABC","ABC,<EOF>",103))
    
    def test_identifier_with_digit(self):
        """test identifier with digit"""
        self.assertTrue(TestLexer.checkLexeme("abc123","abc123,<EOF>",104))
        
    def test_identifier_with_underscore(self):
        """test identifier with underscore"""
        self.assertTrue(TestLexer.checkLexeme("abc_a _ac","abc_a,_ac,<EOF>",105))
    
    def test_identifier_with_underscore_and_digit(self):
        """test identifier with underscore and digit"""
        self.assertTrue(TestLexer.checkLexeme("abc_123 _ac_123","abc_123,_ac_123,<EOF>",106))
    def test_identifier_with_digit_and_wrong_token(self):
        """test identifier with wrong token"""
        self.assertTrue(TestLexer.checkLexeme("abc_123.3","abc_123,.,3,<EOF>",107))
    def test_wrong_digit_as_identifier(self):
        """test digit as identifier"""
        self.assertTrue(TestLexer.checkLexeme("12ab","12,ab,<EOF>",108))
    def test_identifier_with_wrong_token(self):
        """test identifier with wrong token"""
        self.assertTrue(TestLexer.checkLexeme("my@variable","my,ErrorToken @",109))
    def test_identifier(self):
        """test identifier"""
        self.assertTrue(TestLexer.checkLexeme("_____my1Age Ch___eck","_____my1Age,Ch___eck,<EOF>",110))
        
    def test_comment_line(self):
        """test comment line"""
        self.assertTrue(TestLexer.checkLexeme("""a b c // comment 
                                              abc""","a,b,c,;,abc,<EOF>",111))
    
    def test_comment_block(self):
        """test comment block"""
        self.assertTrue(TestLexer.checkLexeme("""/* comment
                                              check comment
                                              this is comment*/ var abc int ;""","""var,abc,int,;,<EOF>""",112))
    
    def test_nested_comment_block(self):
        """test nested comment block"""
        self.assertTrue(TestLexer.checkLexeme("""/* comment
                                              /*check nested*/
                                              this is comment*/ var abc int ;""","""var,abc,int,;,<EOF>""",113))
    def test_multi_nested_comment_block(self):
        """test multi comment block"""
        self.assertTrue(TestLexer.checkLexeme("""/* comment
                                              /*check comment
                                              this is comment*/ /* comment
                                              check comment
                                              this is comment*/*/ var a int;""","""var,a,int,;,<EOF>""",114))
    def test_nested_comment_block_unclosed(self):
        """test nested comment block unclosed"""
        self.assertTrue(TestLexer.checkLexeme("""/* comment
                                              /*check comment
                                              this is comment*/""","""<EOF>""",115))
    
    def test_comment_block_unclosed(self):
        """test comment block unclosed"""
        self.assertTrue(TestLexer.checkLexeme("""/* comment
                                              check comment
                                              this is comment""","""/,*,comment,;,check,comment,;,this,is,comment,<EOF>""",116))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",117))
    
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",118))
    def test_keyword_if(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("if x== y","if,x,==,y,<EOF>",119))
    def test_keyword_else(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("else x := y","else,x,:=,y,<EOF>",120))
    def test_keyword_for_and_range(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme(
        """for index, value := range array {
            // statements
        }""","for,index,,,value,:=,range,array,{,},<EOF>",121))
    def test_complex_keyword(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("if else for break continue return","if,else,for,break,continue,return,<EOF>",122))
    def test_keyword_with_wrong_token(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("if?elsea","if,ErrorToken ?",123))

    # INT, DIGIT
        
    def test_digit_decint(self):
        """test digit"""
        self.assertTrue(TestLexer.checkLexeme("1203 989","1203,989,<EOF>",124))
    
    def test_decint_with_zero_first(self):
        """test int with zero first"""
        self.assertTrue(TestLexer.checkLexeme("001203 0989","0,0,1203,0,989,<EOF>",125))
    
    
    # FLOAT
    def test_float(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("0.123 989.989","0.123,989.989,<EOF>",126))
        
    def test_float_with_e(self):
        """test float with e"""
        self.assertTrue(TestLexer.checkLexeme("123.123e123 989.989E989","123.123e123,989.989E989,<EOF>",127))
    
    def test_float_with_wrong_e(self):
        """test float with wrong e"""
        self.assertTrue(TestLexer.checkLexeme("123.123E 23e","123.123,E,23,e,<EOF>",128))
    def test_float_with_wrong_e_and_float(self):
        """test float with wrong e and digit"""
        self.assertTrue(TestLexer.checkLexeme("0123.123e123.123","0123.123e123,.,123,<EOF>",129))
    
    def test_float_with_e_and_sign(self):
        """test float with e and sign"""
        self.assertTrue(TestLexer.checkLexeme("0123.123e+0000123 989.989e-0989","0123.123e+0000123,989.989e-0989,<EOF>",130))
    
    def test_float_with_e_and_wrong_sign(self):
        """test float with e and wrong sign"""
        self.assertTrue(TestLexer.checkLexeme("00123.123e+-989","00123.123,e,+,-,989,<EOF>",131))
    
    def test_float_with_e_and_wrong_sign_and_float(self):
        """test float with e and wrong sign and float"""
        self.assertTrue(TestLexer.checkLexeme("123.123e+123.123","123.123e+123,.,123,<EOF>",132))
    
    def test_float_with_e_and_wrong_sign_and_float_and_e(self): 
        """test float with e and wrong sign and float and e"""
        self.assertTrue(TestLexer.checkLexeme("123.123e+123.123e5","123.123e+123,.,123,e5,<EOF>",133))
        
        
    # BININT
    def test_BININT(self):
        """test BININT"""
        self.assertTrue(TestLexer.checkLexeme("0b10101 0B10101","0b10101,0B10101,<EOF>",134))
        
    def test_BININT_with_wrong_digit(self):
        """test BININT with wrong digit"""
        self.assertTrue(TestLexer.checkLexeme("0b10102101","0b1010,2101,<EOF>",135))
        
    def test_BININT_with_wrong_digit_and_wrong_token(self):
        """test BININT with wrong digit and token"""
        self.assertTrue(TestLexer.checkLexeme("0b1010a","0b1010,a,<EOF>",136))
    def test_wrong_token_BININT(self):
        """test BININT with wrong token"""
        self.assertTrue(TestLexer.checkLexeme("4b1010","4,b1010,<EOF>",137))
        
        
    # OCTINT
    
    def test_OCTINT(self):
        """test OCINT"""
        self.assertTrue(TestLexer.checkLexeme("0o123 0O123","0o123,0O123,<EOF>",138))
    
    def test_OCTINT_with_wrong_digit(self):
        """test OCTINT with wrong digit"""
        self.assertTrue(TestLexer.checkLexeme("0o128","0o12,8,<EOF>",139))
        
    def test_OCTINT_with_wrong_digit_and_wrong_token(self):
        """test OCTINT with wrong digit and token"""
        self.assertTrue(TestLexer.checkLexeme("0o12a","0o12,a,<EOF>",140))   
    
    def test_OCINT_with_wrong_token(self):
        """test OCTINT with wrong token"""
        self.assertTrue(TestLexer.checkLexeme("0o1?2","0o1,ErrorToken ?",141)) 
    def test_OCTINT_with_no_space(self):
        """test OCTINT with no space"""
        self.assertTrue(TestLexer.checkLexeme("0o120o12","0o120,o12,<EOF>",142))
    def test_wrong_token_OCTINT(self):
        """test OCTINT with wrong token"""
        self.assertTrue(TestLexer.checkLexeme("4o1070","4,o1070,<EOF>",143))
        
        
    # HEXINT
    def test_HEXINT_only_digits(self):
        """test HEXINT"""
        self.assertTrue(TestLexer.checkLexeme("0x123 0X123","0x123,0X123,<EOF>",144))
    def test_HEXINT_only_lower_upper(self):
        """test HEXINT"""
        self.assertTrue(TestLexer.checkLexeme("0xaBc 0XABc","0xaBc,0XABc,<EOF>",145))
    def test_HEXINT_with_all(self):
        """test HEXINT"""
        self.assertTrue(TestLexer.checkLexeme("0x123abc 0X123ABC","0x123abc,0X123ABC,<EOF>",146))
        
    def test_HEXINT_with_wrong_digit(self):
        """test HEXINT with wrong digit"""
        self.assertTrue(TestLexer.checkLexeme("0x12g","0x12,g,<EOF>",147))
    def test_HEXINT_with_no_space(self):
        """test HEXINT with OCTINT"""
        self.assertTrue(TestLexer.checkLexeme("0x120X12","0x120,X12,<EOF>",148))
    def test_HEXINT_with_wrong_token(self):
        """test HEXINT with wrong token"""
        self.assertTrue(TestLexer.checkLexeme("0x12?","0x12,ErrorToken ?",149))
    
    def test_complex_Hexint(self):
        """test complex HEXINT"""
        self.assertTrue(TestLexer.checkLexeme("0x123abc 0X123ABCDEX0 0xabc2","0x123abc,0X123ABCDE,X0,0xabc2,<EOF>",150))
    
    # string
    
    def test_string (self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "MiniGo" """,""""MiniGo",<EOF>""",151))
    def test_assign_string(self):
        """test assign string"""
        self.assertTrue(TestLexer.checkLexeme(""" s:= "MiniGo  Hello MiniGo check" ""","""s,:=,"MiniGo  Hello MiniGo check",<EOF>""",152))
    def test_unclosed_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "MiniGo  Hello MiniGo check ""","""Unclosed string: "MiniGo  Hello MiniGo check """,153))
    def test_unclosed_string_with_newline(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Minigo\n" ""","""Unclosed string: "Minigo""",154))
    def test_string_with_escape(self):
        """test string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "MiniGo  \\" Hello MiniGo \\n \\\\check" """,""""MiniGo  \\" Hello MiniGo \\n \\\\check",<EOF>""",155))
    def test_string_with_escape_2(self):
        """test string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "MiniGo  \\t Hello MiniGo \\r check \\nMiniGo check" """,""""MiniGo  \\t Hello MiniGo \\r check \\nMiniGo check",<EOF>""",156))
        
    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.checkLexeme(""" "Minigo" Helloworld "test string" """,""""Minigo",Helloworld,"test string",<EOF>""",157))
    
    def test_complex_string_with_escape(self):
        """test complex string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "Minigo" Helloworld "test string \\n \\"" """,""""Minigo",Helloworld,"test string \\n \\"",<EOF>""",158))
    def test_string_with_illegal_escape(self):
        """test string with illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "test escape \\n hell\\o world" ""","""Illegal escape in string: "test escape \\n hell\\o""",159))
    def test_complex_string_with_illegal_escape(self):
        """test string with escape"""
        self.assertTrue(TestLexer.checkLexeme(' "Minigo" Helloworld "test string \\k \\"" ','"Minigo",Helloworld,Illegal escape in string: "test string \\k',160))
    def test_null_string(self):
        """test null string"""
        self.assertTrue(TestLexer.checkLexeme(""" "" """,""""",<EOF>""",161))
        
    def test_string_illegal_escape_and_unclosed(self):
        """test string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "test string \\t \\" """,'Unclosed string: "test string \\t \\" ',162))
        
    #operator
    
    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("+=-=*=/=%=","+=,-=,*=,/=,%=,<EOF>",163))
    def test_operator2(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("+-*/%","+,-,*,/,%,<EOF>",164))
    def test_operator_compare(self):
        """test operator compare"""
        self.assertTrue(TestLexer.checkLexeme("== != < > <= >=","==,!=,<,>,<=,>=,<EOF>",165))
    def test_operator_boolean(self):
        """test operator boolean"""
        self.assertTrue(TestLexer.checkLexeme("&& || !","&&,||,!,<EOF>",166))
    
    def test_mix_int_operator(self):
        """test mix int operator"""
        self.assertTrue(TestLexer.checkLexeme("123+456-789*123/456%789","123,+,456,-,789,*,123,/,456,%,789,<EOF>",167))
    def test_mix_float_operator(self):
        """test mix float operator"""
        self.assertTrue(TestLexer.checkLexeme("000123.123+456.456-789.789*123.123/456.456%789.789","000123.123,+,456.456,-,789.789,*,123.123,/,456.456,%,789.789,<EOF>",168))
    
    def test_complex_operator(self):
        """test complex operator"""
        self.assertTrue(TestLexer.checkLexeme("++=--=-===>=<+!||","+,+=,-,-=,-=,==,>=,<,+,!,||,<EOF>",169))
    
    #seperator
    
    def test_seperator(self):
        """test seperator"""
        self.assertTrue(TestLexer.checkLexeme("()[]{};,","(,),[,],{,},;,,,<EOF>",170))
    def test_func_with_seperator(self):
        """test func with seperator"""
        self.assertTrue(TestLexer.checkLexeme("func main ( ) { }","func,main,(,),{,},<EOF>",171))
    def test_seperator_with_digit(self):
        """test seperator with digit"""
        self.assertTrue(TestLexer.checkLexeme("123(456)789[123]{}","123,(,456,),789,[,123,],{,},<EOF>",172))
        
        
    # array
    
    def test_array(self):
        """test array"""
        self.assertTrue(TestLexer.checkLexeme("[1,2,3]","[,1,,,2,,,3,],<EOF>",173))
    def test_array_with_operator(self):
        """test array with operator"""
        self.assertTrue(TestLexer.checkLexeme("[1+2,3-4,5*6,7/8,9%10]","[,1,+,2,,,3,-,4,,,5,*,6,,,7,/,8,,,9,%,10,],<EOF>",174))
    def test_array_with_float(self):
        """test array with float"""
        self.assertTrue(TestLexer.checkLexeme("[1.1,2.2,3.3]","[,1.1,,,2.2,,,3.3,],<EOF>",175))
    def test_array_with_string(self):
        """test array with string"""
        self.assertTrue(TestLexer.checkLexeme("""["Minigo","Hello","World"]""","""[,"Minigo",,,"Hello",,,"World",],<EOF>""",176))
    def test_array_with_array(self):
        """test array with array"""
        self.assertTrue(TestLexer.checkLexeme("[[1,2],[3,4],[5,6]]","[,[,1,,,2,],,,[,3,,,4,],,,[,5,,,6,],],<EOF>",177))
        
        
    # negative
    def test_negative_int(self):
        """test negative int"""
        self.assertTrue(TestLexer.checkLexeme("-123 + 90 + -100","-,123,+,90,+,-,100,<EOF>",178))
    def test_negative_float(self):
        """test negative float with operator"""
        self.assertTrue(TestLexer.checkLexeme("-123.123 + -123.123","-,123.123,+,-,123.123,<EOF>",179))
    def test_negative_float_e(self):
        """test negative float with e"""
        self.assertTrue(TestLexer.checkLexeme("123.0e-123 + 123.0e-123","123.0e-123,+,123.0e-123,<EOF>",180))
        
    # type struct class interface const func
    def test_type(self):
        """test type"""
        self.assertTrue(TestLexer.checkLexeme("int float bool string","int,float,bool,string,<EOF>",181))
    def test_complex_type(self):
        """test complex type"""
        self.assertTrue(TestLexer.checkLexeme("int float bool string int[] float[] bool[] string[]","int,float,bool,string,int,[,],float,[,],bool,[,],string,[,],<EOF>",182))
    def test_struct_declare(self):
        """test struct declare"""
        self.assertTrue(TestLexer.checkLexeme("type Student struct { }","type,Student,struct,{,},<EOF>",183))
    def test_class_with_dot_operator(self):
        """test class with dot operator"""
        self.assertTrue(TestLexer.checkLexeme("Student.name","Student,.,name,<EOF>",184))
    def test_struct_with_field(self):
        """test struct with field"""
        self.assertTrue(TestLexer.checkLexeme("type Student struct { name string }","type,Student,struct,{,name,string,},<EOF>",185))
    def test_interface_declare(self):
        """test interface declare"""
        self.assertTrue(TestLexer.checkLexeme("type Student interface { }","type,Student,interface,{,},<EOF>",186))
    def test_const_declare(self):
        """test const declare"""
        self.assertTrue(TestLexer.checkLexeme("const PI = 3.14","const,PI,=,3.14,<EOF>",187))
    def test_func_with_return(self):
        """test func with return"""
        self.assertTrue(TestLexer.checkLexeme("func main ( ) int { return 1 }","func,main,(,),int,{,return,1,},<EOF>",188))
        
        
    # complex
    def test_mix_func_with_param_int(self):
        """test func with param int"""
        self.assertTrue(TestLexer.checkLexeme('println(10);','println,(,10,),;,<EOF>',189))
    def test_mix_func_with_param_string(self):
        """test func with param string"""
        self.assertTrue(TestLexer.checkLexeme('println("x is equal to 10");','println,(,"x is equal to 10",),;,<EOF>',190))
        
    def test_multiline_complex_scenario(self):
        self.assertTrue(TestLexer.checkLexeme("""// Initialize variables
        x := 10 // int
        y := 20.5
        z := "hello"
        arr := [1, x, y]""","""x,:=,10,;,y,:=,20.5,;,z,:=,"hello",;,arr,:=,[,1,,,x,,,y,],<EOF>""",191))
    
    def test_method_call(self):
        self.assertTrue(TestLexer.checkLexeme("student.getName()","student,.,getName,(,),<EOF>",192))
    
    def test_method_call_with_param(self):
        self.assertTrue(TestLexer.checkLexeme("""student.setName("Minigo")""","""student,.,setName,(,"Minigo",),<EOF>""",193))
        
    def test_matrix(self):
        self.assertTrue(
            TestLexer.checkLexeme("arr[2][3] := b[2] + 1", "arr,[,2,],[,3,],:=,b,[,2,],+,1,<EOF>", 194))

    def test_array_mixed_types(self):
        """test array with mixed types"""
        self.assertTrue(TestLexer.checkLexeme("[1, \"string\", true, 3.14]", "[,1,,,\"string\",,,true,,,3.14,],<EOF>", 195))

    def test_complex_with_loop(self):
        """test complex with loop"""
        self.assertTrue(TestLexer.checkLexeme("""for i:=0;i<10;i++{println(i)}""","""for,i,:=,0,;,i,<,10,;,i,+,+,{,println,(,i,),},<EOF>""",196))
    def test_complex_with_continue(self):
        """test complex with continue"""
        self.assertTrue(TestLexer.checkLexeme("""for i := 0; i < 10; i++ {if (i == 5) {continue;}// statements that will not execute when i == 5 \n}""",
                                              """for,i,:=,0,;,i,<,10,;,i,+,+,{,if,(,i,==,5,),{,continue,;,},;,},<EOF>""",197))


    def test_illegal_tokens(self):
        """test illegal tokens"""
        self.assertTrue(TestLexer.checkLexeme("$%^&*", "ErrorToken $", 198))

    def test_auto_semi(self):
        self.assertTrue(TestLexer.checkLexeme("""const \n x =\n3
                                              var y \n = 10""", "const,x,=,3,;,var,y,;,=,10,<EOF>", 199))
        
    def test_auto_semi_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" func(){
            //test
            }
            x:=
            10""", "func,(,),{,},;,x,:=,10,<EOF>", 200))
    
    def test_110(self):
        input_str = "\"hello\r\nworld\""
        expected = "0,321123,0b2121,0B2122,0o21,0O2111,0x1FFFF,0Xa2A,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input_str, expected, 1))
        
