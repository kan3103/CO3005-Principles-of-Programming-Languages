//2211437
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {

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
}

options{
	language=Python3;
}

program : decl program_tail;

program_tail : decl program_tail | EOF;


decl: funcdecl | vardecl | typedecl ;


//VAR
vardecl: vararray| var | const; 

var: VAR ID alltype AS2 expr SEMI | VAR ID alltype SEMI | VAR ID AS2 expr SEMI;

vararray: VAR ID space_array alltype AS2 expr SEMI | VAR ID space_array alltype SEMI;

const: CONST ID AS2 expr SEMI;

alltype: STRING | INTTYPE | FLOAT | BOOLEAN | ID;


//FUNCTION

list_id: ID | list_id COMMA ID;

funcdecl: FUNC ID param functype funcbody SEMI | funcstruct;

functype: space_array_op alltype | ;

param:LB parammethod RB | LB RB;

funcbody: LC list_stmts RC;

funcstruct: FUNC LB ID space_array_op alltype RB ID param functype funcbody SEMI;

//STATEMENTS

list_stmts: stmts | list_stmts stmts;

stmts: assign_stmts | if_stms | call_stmts | continue_stmt | break_stmt | vardecl | return_stmt | for_stmt;

continue_stmt: CONTINUE SEMI;
break_stmt: BREAK SEMI;
return_stmt: RETURN expr SEMI | RETURN SEMI;
call_stmts: method_element  SEMI | funccall SEMI;

for_stmt: for_condition | for_update | for_array;
for_condition: FOR expr funcbody SEMI;
for_update: FOR ID assign expr SEMI expr SEMI ID assign expr funcbody SEMI;
for_array: FOR ID COMMA ID AS1 RANGE expr funcbody SEMI ;

assign_stmts: lhs_assign assign expr SEMI;
lhs_assign: ID | access_struct | array_element;
assign: AS1 | ADDAS | MiNUSAS | MULAS | DIVAS | MODAS;

if_stms: IF condition funcbody ifelse ELSE funcbody SEMI | IF condition funcbody ifelse  SEMI ; 
ifelse: ELSE IF condition funcbody | ifelse ELSE IF condition funcbody |;
condition: LB expr RB;


// EXPRESSION

expr_list: expr | expr_list COMMA expr;

expr: or_expr ;
or_expr: or_expr OR and_expr | and_expr;
and_expr: and_expr AND logic_expr | logic_expr ;

logic_expr: logic_expr compare add_expr | add_expr ;

compare:EQUAL 
    | NEQUAL 
    | BIG 
    | SMALL 
    | EBIG
    | ESMALL;

add_expr: add_expr ADD mul_expr | add_expr MINUS mul_expr | mul_expr;
mul_expr: mul_expr MUL neg_expr | mul_expr DIV neg_expr | mul_expr MOD neg_expr | neg_expr;
neg_expr: MINUS  neg_expr | NOT neg_expr | element_expr ;

element_expr: method_element | array_element | access_struct | factor_expr;

struct_expr: factor_expr | struct_expr postfix;
postfix: access_field | method_op | index_op;
factor_expr: LB expr RB | literal | ID | funccall;

access_struct: struct_expr access_field;
method_element: struct_expr method_op;
array_element: struct_expr index_op;

access_field: DOT ID;
method_op: DOT funccall ;
index_op: LS expr RS ;
funccall: ID LB expr_list RB | ID LB RB;

// TYPE
typedecl:  type_stuct | type_inter;

type_stuct: TYPE ID STRUCT body_type SEMI;

type_inter: TYPE ID INTERFACE LC body_inter RC SEMI;

body_inter: ID LB parammethod_op RB functype SEMI |body_inter ID LB parammethod_op RB  functype SEMI;

parammethod_op: parammethod |;
parammethod: list_id space_array_op alltype | parammethod COMMA list_id space_array_op alltype;


body_type: LC body_body_type RC;
body_body_type: ID space_array_op alltype SEMI | body_body_type  ID space_array_op alltype SEMI;


// LITERAL

literal:array | struct_literal | BOOLITERAL | INT | REAL | STRINGLIT |  ID  | NIL;

literal_array: struct_literal| BOOLITERAL | INT | REAL | STRINGLIT | ID  | NIL | array_list;

BOOLITERAL: TRUE | FALSE;

space_array: LS ID RS space_array_op | LS INT RS space_array_op ;

space_array_op: space_array | ;

array: space_array  alltype array_list;

array_nested: literal_array | literal_array COMMA array_nested;


array_list: LC array_nested RC;

struct_literal: ID LC struct_param RC | ID LC RC;
struct_param: ID COLON expr | struct_param COMMA  ID COLON expr;


// LEXER

IF:'if';
ELSE: 'else';
TRUE:'true';
FALSE:'false';
FOR:'for';
RANGE:'range';
BREAK:'break';
CONTINUE:'continue';
RETURN:'return';
FUNC:'func';
TYPE:'type';
STRUCT:'struct';
INTERFACE:'interface';
VAR:'var';


STRING:'string';
INTTYPE:'int';
FLOAT:'float';
BOOLEAN:'boolean';
CONST:'const';
NIL: 'nil';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;


INT: DECINT|OCTINT|BININT|HEXINT;
DECINT: '0'|[1-9] DIGIT*;
BININT: ('0b'|'0B') [01]+;
OCTINT: ('0O'|'0o') [0-7]+;
HEXINT: ('0x'|'0X') [0-9a-fA-F]+;


REAL: DIGIT+ '.' DIGIT* EXPONENT?;

fragment DIGIT: [0-9];
fragment EXPONENT: [eE] [+-]? DIGIT+; 


ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';

ADDAS : '+=';
MiNUSAS: '-=';
MULAS: '*=';
DIVAS: '/=';
MODAS: '%=';

EQUAL : '==';
NEQUAL: '!=';
BIG: '>';
SMALL: '<';
EBIG: '>=';
ESMALL: '<=';
NOT: '!';

AND:'&&';
OR: '||';

LB: '(';
RB: ')';

LS: '[';
RS: ']';

LC: '{';
RC: '}';

COMMA: ',';
SEMI: ';';
COLON: ':';

DOT: '.';
AS1: ':=';
AS2: '=';


STRINGLIT: '"' (STRING_CHAR|IllEscape)*? '"'{ 
    self.text = self.text.strip('\n')
    self.text = self.text.strip('\r')
    self.text = self.text.strip('\f')
} ;

fragment STRING_CHAR: ~["\\\n];
fragment IllEscape: '\\' ('t'|'n'|'r'|'"'|'\\');


NL: '\n' {
    if self.handle():
        self.text = ';'
        self.type = self.SEMI
    else:
        self.skip()
};


WS : [ \t\r\f]+  -> skip ; // skip spaces, tabs , form feed


COMMENT1: '//' ~[\n]* -> skip ; // skip comment in line
COMMENT2: '/*' (COMMENT2| .)*? '*/'->skip ;

UNCLOSE_STRING: '"' (STRING_CHAR|IllEscape)* [\n\f]? {
    self.text = self.text.strip('\n')
    self.text = self.text.strip('\r')
    self.text = self.text.strip('\f')
};
ILLEGAL_ESCAPE: '"' (STRING_CHAR|IllEscape)*? '\\' ~('t'|'n'|'r'|'"'|'\\');
ERROR_CHAR: .;



