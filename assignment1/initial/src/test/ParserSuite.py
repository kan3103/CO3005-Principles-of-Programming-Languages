import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "Error on line 1 col 14: }"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
            var x int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_var_declare_with_type(self):
        input = """var a int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    
    def test_var_declare_with_initialization(self):
        input = """var a = 0 
        var s= "string";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_var_declare_with_full(self):
        input = """var a int = 0;
        var s string = "string";
        var b boolean = true;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))   
    
    def test_var_declare_with_complex(self):
        input = """var a int = x+2-4;
        var s string = "string"+""+x;
        var b boolean = true||false;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test_array_declare(self):
        input = """var arr [5]int; // defines an array of 5 integers."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    def test_array_declare_multi(self):
        input = """var multi_arr [2][5]int; // defines an array of 2 x 5 integers."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
        
    def test_array_declare_with_const(self):
        input = """var arr [var_const]int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    
    def test_array_with_wrong_size(self):
        input = """var arr [5.8]int; """
        expect = "Error on line 1 col 10: 5.8"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    
    def test_array_with_other_type(self):
        input = """var arr [5]float; 
        var arr2 [5]boolean;
        var arr3 [5]string;
        var arr4 [5]Test;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    
    def test_struct_declare(self):
        input = """type Point struct{
            x int; y int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    
    def test_struct_declare_with_array(self):
        input = """type Point struct{
            x int; y int; arr [5]int;
            Point p;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test_struct_declare_with_struct(self):
        input = """type Point struct{
            x int; y int; arr [5]int;
            Point p;
        };
        type Line struct{
            p1 Point; p2 Point;
        };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    
    def  test_func_struct_declare(self):
        input = """func (p Person) Greet() string {
                    return "Hello, " + p.name
                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    
    def test_func_struct_declare_with_param(self):
        input = """func (p Person) Greet(name string) string {
                    return "Hello, " + name
                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    
    def test_stuct_and_func_declare(self):
        input = """ 
        type Point struct{ x int; y int; }; func(p Point) distance(p2 Point) float { return sqrt((p.x - p2.x)*(p.x - p2.x) + (p.y - p2.y)*(p.y - p2.y)); };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
        
    def test_interface_declare(self):
        input = """type Calculator interface {
        Add(x, y int) int;
        Subtract(a, b float, c int) float;
        Reset()
        SayHello(name string)
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
        
    def test_interface_declare2(self):
        input = """type I interface {
        f(x,y,z int)
        g()
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
        
    def test_func_declare(self):
        input = """func  Add() int {
                    return x + y;
                    };"""   
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
        
    def test_func_declare_with_param(self):
        input = """func  Add(x int, y int) int {
                    return x + y;
                    };"""   
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
        
    def test_func_declare_with_newline(self):
        input = """func main() 
        {
                    return 
                    };"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,225))
        
    def test_func_declare_with_array_type(self):
        input = """func  Add(x [5]int, y [5]int) [5]int {
                    return x + y;
                    };"""   
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_declare_without_semicolon(self):
        input = """var a int =
        10
        var b int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_declare_without_semicolon2(self):
        input = """var a int \n= 10
        var b int;"""
        expect = "Error on line 2 col 1: ="
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_declare_without_semicolon3(self):
        input = """var a\nint \n= 10
        var b int
        var c int;"""
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test_declare_with_wrong_keyword(self):
        input = """var true int = 10;"""
        expect = "Error on line 1 col 5: true"
        self.assertTrue(TestParser.checkParser(input,expect,230))
        
    def test_const_declare(self):
        input = """const a = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    
    def test_wrong_const_declare(self):
        input = """const a float = 10"""
        expect = "Error on line 1 col 9: float"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    
    def test_add_expression(self):
        input = """func main() {
                    a := 5 + 6;
                    test := a + 5;
                    check:= test + a + 5;
                    check:= test + a + 5 - -6;
                    test := a + 5 - 6;
                    test:= a + 5 - 6 + 7;
                    test:= 10.e-2 + 5;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    def test_mul_expression(self):
        input = """func main() {
                    a := 5 * 6;
                    test := a * 51;
                    check:= test * a * 5;
                    check:= test * a * 5 / 6;
                    test := a * 5 / 6.31;
                    test:= a * 5.746 / 6 * 72;
                    check:= 10.e-2 * 5;
                    check:= 10.e-2 * 5 / 6 %7;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    
    def test_expression_with_parentheses(self):
        input = """func main() {
                    a := (5 + 6);
                    test := (a + 5);
                    check:= (test + a + 5);
                    check:= (test + a + 5) - (-6);
                    test := (a + 5) - 6;
                    test:= (a + 5) - 6 + 7;
                    test:= (10.e-2) + 5;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    
    def test_complex_arithmetic_expression(self):
        input = """func main() {
                    a := (5 + 6) * 5;
                    test := (a + 5) / 6;
                    check:= (test + a + 5) % 6;
                    check:= (test + a + 5) - (-6);
                    test := (a + 5) - 6;
                    test:= (a + 5) - 6 + 7;
                    test:= (10.e-2) + 5;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
        
    def test_wrong_parenthese(self):
        input = """func main() {
                    a := (5 + 6 * 5;
                    test := a + 5);
                    check:= test + a + 5);
                    check:= test + a + 5 - -6);
                    test := a + 5 - 6);
                    test:= a + 5 - 6 + 7);
                    test:= 10.e-2 + 5);
                };"""
        expect = "Error on line 2 col 36: ;"
        self.assertTrue(TestParser.checkParser(input,expect,237))
        
    def test_boolean_expression(self):
        input = """func main() {
                    a := true;
                    b := false;
                    c := a && b;
                    d := a &&( c || b);
                    e := !a;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_wrong_boolean_expression(self):
        input = """func main() {
                    a := true;
                    b := false;
                    c := a && b;
                    d := a || b;
                    e := !a;
                    f := a && b &&;
                    g := a || b ||;
                    h := !a!;
                };"""
        expect = "Error on line 7 col 35: ;"
        self.assertTrue(TestParser.checkParser(input,expect,239))
        
    def test_access_array(self):
        input = """func main() {
                    a := arr[5];
                    b := arr[5][6];
                    c := arr[5][6][7];
                    d := arr[5][6][7][8];
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    
    def test_access_array_with_expression(self):
        input = """func main() {
                    a := arr[5+6];
                    b[2] := arr[5][6*7];
                    c[3][2-4] := arr[true][6][7-8];
                    d := arr[5][hi-34][test()][8/9];
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
        
    def test_access_array_with_wrong(self):
        input = """func main() {
                    a := arr[5+6];
                    b[i] := arr[5][6*7;
                    c := arr[true][6][7-8;
                    d := arr[5][hi-34][test()][8/9;
                };"""
        expect = "Error on line 3 col 39: ;"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    
    def test_array_literal(self):
        input = """func main() {
                    a := [5]int{1,2,3,4,5};
                    b := [2]boolean{true,false};
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
        
    def test_array_literal_with_expression(self):
        input = """func main() {
                    a := [5]int{1+2,2*3,3/4,4-5,5};
                    b := [2]boolean{true&&false,false};
                };"""
        expect = "Error on line 2 col 34: +"
        self.assertTrue(TestParser.checkParser(input,expect,244))
        
    def test_multi_array_literal(self):
        input = """func main() {
                    a := [5][6]int{{1,2,3,4,5,6},{7,8,9,10,11,12},{13,14,15,16,17,18},{19,20,21,22,23,24},{25,26,27,28,29,30}};
                    b := [2][3]boolean{{true,false,true},{false,true,false}};
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
        
    def test_array_literal_with_function_call(self):
        input = """func main() {
                    a := [5]int{test(),test2(),test3(),test4(),test5()};
                    b := [2]boolean{test(),test2()};
                };"""
        expect = "Error on line 2 col 37: ("
        self.assertTrue(TestParser.checkParser(input,expect,246))
        
    def test_array_literal_with_wrong(self):
        input = """func main() {
                    a := [5]int{1,2,3,4,5;
                    b := [2]boolean{true,false};
                };"""
        expect = "Error on line 2 col 42: ;"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    
    def test_array_literal_in_function_call(self):
        input = """func main() {
                    a := test([5]int{1,2,3,4,5});
                    b := test2([2]boolean{true,false});
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_access_struct(self):
        input = """func main() {
                    a := p.x;
                    b := p.y;
                    c := p.arr[5];
                    d := p.arr[5][6];
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
        
    def test_multi_access_struct(self):
        input = """func main() {
                    a := p.x + 5;
                    b := p.y.x.y.qe - 6;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    
    def test_access_struct_with_expression(self):
        input = """func main() {
                    a := p.x + 5;
                    b := p.y - 6;
                    c := p.arr[5+6];
                    d := p.arr[5][6*7];
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    
    def test_access_method(self):
        input = """func main() {
                    a := p.distance(p2);
                    b := p.distance(p2) + 5;
                    c := p.distance(p2) - 6;
                    d := p.distance(p2) * 7;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
        
    def test_complex_access_method_and_attributes(self):
        input = """func main() {
                    a := p.check().t + 5;
                    b := p.t.check().test().a - 6;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    
    def test_function_call(self):
        input = """func main() {
                    a := test();
                    b := test(5);
                    c := test(5,6);
                    d := test(5,6,7);
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    def test_function_call_with_expression(self):
        input = """func main() {
                    a := test(5+61);
                    b := test(5*6-p.x);
                    c := test(5/6);
                    d := test(p.get());
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_function_call_wrong(self):
        input = """func main() {
                    a := test(5+61);
                    b := test(5*6-p.x);
                    c := test(5/6;
                    d := test(p.get());
                };"""
        expect = "Error on line 4 col 34: ;"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_function_call_wrong2(self):
        input = """func main() {
                    a := test(5+61);
                    b := test(5*6-p.x);
                    c := test(5/6);
                    d := test(p.get();
                };"""
        expect = "Error on line 5 col 38: ;"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    
    def test_function_call_with_array(self):
        input = """func main() {
                    a := test([2]int{1,2});
                    b := test(arr[5]);
                    c := test(arr[5][6]-arr[2]);
                    d := test(arr[5][6][7]);
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    
    def test_function_call_and_array(self):
        input = """func main() {
                    arr[6] := test()[2];
                    arr[6] := test(a,b)[2][3];
                    arr[6] := test()[2][3][4];
                    arr[7] := test(x,y,z)[2][3][4][5];
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    
    def test_function_call_with_struct(self):
        input = """func main() {
                    a := test(p.rt.test((p2)));
                    arr[2]:= test(p.r.r.r.test().r);
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    
    def test_function_call_expression_and_method(self):
        input = """func main() {
                    a:= test().test(p2);
                    b:= test().test(p2).test(p3);
                    c:= test().c.c
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    
        
    def test_complex_expression_with_array_funccal_method(self):
        input = """func main() {
                    a:= test.arr[5].test(p2)[2];
                    b:= test().test(p2).test(p3);
                    c:= test().c.c[2].check(test())
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
        
    def test_function_call_statement(self):
        input = """func main() {
                    test();
                    arr[2].test(5);
                    p.test(5,6);
                    p[check].test(5,6,7);
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    
    def test_struct_literal(self):
        input = """func main() {
                    a := Point{check:1 , x:2, y:3};
                    b := Point{x:-22, y:3};
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    
    def test_struct_literal_with_expression(self):
        input = """func main() {
                    a := Point{check:1 , x:2, y:3};
                    b := Point{x:-22, y:3-2+px};
                    d := Point{x:arr[2][5]-test(), y:3-2+px};
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    
    def test_struct_literal_with_wrong(self):
        input = """func main() {
                    a := Point{check:1 , x:2, y:3;
                    b := Point{x:-22, y:3};
                };"""
        expect = "Error on line 2 col 50: ;"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_struct_literal_with_struct_literal(self):
        input = """func main() {
                    a := Point{check:1 , x:2, y:3, p:Point{x:1,y:2}};
                    b := Point{x:-22, y:3, p:Point{x:1,y:2}};
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
        
    def test_null_struct_literal(self):
        input = """func main() {
                    a := Point{};
                    b := Point{};
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    
    def test_on_one_line(self):
        input = """type Rectangle struct { w int; h int; }; func main() {a := 5; b := 6; c := a + b; d := c;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    
    def test_on_one_line_without_semicolon(self):
        input = """type Rectangle struct { w int; h int; } func main() {a := 5; b := 6; c := a + b; d := c;}"""
        expect = "Error on line 1 col 41: func"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    
    def test_assign_statement(self):
        input = """func main() {
                    a := 5;
                    b[2] := a;
                    c := b;
                    d := c;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_assign_statement_other(self):
        input = """func main() {
                    a += 5;
                    b[2] -= a+jf -3;
                    test *= b;
                    check /= c;
                    mod %= (d-ie)*3;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
        
    def test_struct_assign_statement(self):
        input = """func main() {
                    p.px := 5;
                    p.py += 6;
                    p.pz -= p.px + p.py;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    
    def test_function_call_assign_statement(self):
        input = """func main() {
                    test():= 5;
                    test(5)-= 6;
                    test(5,6)%=1;
                    test(5,6,7) *= 8;
                };"""
        expect = "Error on line 2 col 27: :="
        self.assertTrue(TestParser.checkParser(input,expect,274))
        
    def test_method_assign_statement(self):
        input = """func main() {
                    p.test() := 5;
                    p.test(5) -= 6;
                    p.test(5,6) %=1;
                    p.test(5,6,7) *= 8;
                };"""
        expect = "Error on line 2 col 30: :="
        self.assertTrue(TestParser.checkParser(input,expect,275))
    
    def test_array_assign_statement(self):
        input = """func main() {
                    arr.px[2].get(2)[1] := 5;
                    arr.px[5] -= 6;
                    arr.arr[5][6][7] %=1;
                    arr[5][6][7][8] *= 8;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
        
    def test_wrong_assign_statement(self):
        input = """func main() {
                    a = 5;
                    b[2] = a;
                    c = b;
                };"""
        expect = "Error on line 2 col 23: ="
        self.assertTrue(TestParser.checkParser(input,expect,277))
        
    def test_statement_without_semicolon(self):
        input = """func main() {
                    cal(a,b)
                    check(a,b)
                    for i:=0;i<10;i+=1{
                        a := a + 1
                    }
                    var b int
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
        
    def test_statement_without_semicolon2(self):
        input = """func main(){
            //test
            x:=
            10
            const 
            a =
            10
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    
    def test_statement_without_semicolon3(self):
        input = """func main(){
            for i:=0
            i<10
            i+=1{
                a := a + 1
            }; continue
            break
            return
            a:=
            a+
            (b+
            c)
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
        
    def test_statement_without_semicolon4(self):
        input = """func main(){
            var a int break
            }
            """
        expect = "Error on line 2 col 23: break"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test_if_statement(self):
        input = """func main() {
                    if (x > 10) {
println("x is greater than 10")
}
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    
    def test_if_else_statement(self):
        input = """func main() {
                    if (x > 10) {
                println("x is greater than 10")
                } else {
                println("x is less than or equal to 10")
                }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    
    
    def test_if_elseif_else_statement(self):
        input = """func main() {
                    if (x > 10) {
                println("x is greater than 10")
                } else if (x == 10) {
                println("x is equal to 10")
                } else {
                println("x is less than 10")
                }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    
    def test_if_statement_with_expression(self):
        input = """func main() {
                    if (x > 10 && y < 20) {
                println("x is greater than 10")
                test()
                check()
                } else if (arr[2]==10||arr[3]==20) {
                println()
                check()
                }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    
    def test_if_statement_with_wrong_newline(self):
        input = """func main() {
                    if (x > 10 && y < 20) {
                println("x is greater than 10")
                test()
                check()
                } 
                else {
                println()
                check()
                }
                };"""
        expect = "Error on line 7 col 17: else"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    
    def test_if_statement_with_wrong(self):
        input = """func main() {
                    if x > 10 && y < 20 {
                        test(x,y)
                    }
                };"""
        expect = "Error on line 2 col 24: x"
        self.assertTrue(TestParser.checkParser(input,expect,287))
        
    def test_for_condition_statement(self):
        input = """func main() {
                    for (x<10) {
                    // statements
                        for true {
                            TEST()
                        }
                    }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    
    def test_for_update_statement(self):
        input = """func main() {
                    for x:=0; x<10; x+=1 {
                    // statements
                        for y:=7; y>0; y-=1 {
                            TEST()
                        }
                    }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    
    def test_for_condition_update_statement_wrong(self):
        input = """func main() {
                    for (x:=0; x<10; x+=1) {
                    // statements
                        for y:=7; y>0; y-=1 {
                            TEST()
                        }
                    }
                };"""
        expect = "Error on line 2 col 27: :="
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_for_with_range_statement(self):
        input = """func main() {
                    for index,value := range arr {
                    // index: 0, 1, 2
                    // value: 10, 20, 30
                        check()
                    }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    
    def test_for_range_without_index_statement(self):
        input = """func main() {
                    for _, value := range arr {
                    // value: 10, 20, 30
                        check()
                    }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    
    def test_break_statement(self):
        input = """func main() {
                    for i:=0; i<10; i+=1 {
                        if (i == 5) {
                            break
                        }
                    }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    
    def test_continue_statement_and_range_array(self):
        input = """func main() {
                    for index,value := range [5]int{1,2,3,4,5} {
                        if (value == 5) {
                            continue
                        }
                    }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    
    def test_for_range_with_wrong(self):
        input = """func main() {
                    for index,value := range "hello" {
                    // index: 0, 1, 2
                    // value: 10, 20, 30
                        check()
                    }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    
    def test_return_statement_without_value(self):
        input = """func main() {
                    return
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    
    def test_return_statement_with_expression(self):
        input = """func main() {
                    return 25+6-7
                }
                
                func test() boolean {
                    return true|| x && y || false
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_emtpy_program(self):
        input = """"""
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    
    def test_function_in_struct(self):
        input = """type Point struct {
                    x int; y int;
                    func (p Point) Greet() string {
                        return 
                    };
                };"""
        expect = "Error on line 3 col 21: func"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    
    def test_unclose_string(self):
        input = """func main() {
                   print("Hello, World!)
                };"""
        expect = "\"Hello, World!)"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    
    def test_for_statement_with_other_array(self):
        input = """func main() {
                    for index,value := range arr[5] {
                    // index: 0, 1, 2
                    // value: 10, 20, 30
                        check()
                    }
                    for index,value := range foo() {
                    // index: 0, 1, 2
                    // value: 10, 20, 30
                        check()
                    }
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))
    def test_access_stuct_array_and_method(self):
        self.assertTrue(TestParser.checkParser("""
            func main() {
                (2+3-(5).a.b[2].x.get(5*4-(39).a[2].add().d)[(3/5).get()]).a[2][2][2][2].a.a.a.a.get().get().dd()[2].a := Person{}
            };
        """, "successful", 302))
    