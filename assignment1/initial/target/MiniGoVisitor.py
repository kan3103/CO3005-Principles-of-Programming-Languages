# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program_tail.
    def visitProgram_tail(self, ctx:MiniGoParser.Program_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var.
    def visitVar(self, ctx:MiniGoParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vararray.
    def visitVararray(self, ctx:MiniGoParser.VararrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const.
    def visitConst(self, ctx:MiniGoParser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#alltype.
    def visitAlltype(self, ctx:MiniGoParser.AlltypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_id.
    def visitList_id(self, ctx:MiniGoParser.List_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functype.
    def visitFunctype(self, ctx:MiniGoParser.FunctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcbody.
    def visitFuncbody(self, ctx:MiniGoParser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcstruct.
    def visitFuncstruct(self, ctx:MiniGoParser.FuncstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_stmts.
    def visitList_stmts(self, ctx:MiniGoParser.List_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmts.
    def visitStmts(self, ctx:MiniGoParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_stmts.
    def visitCall_stmts(self, ctx:MiniGoParser.Call_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_condition.
    def visitFor_condition(self, ctx:MiniGoParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_update.
    def visitFor_update(self, ctx:MiniGoParser.For_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_array.
    def visitFor_array(self, ctx:MiniGoParser.For_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_stmts.
    def visitAssign_stmts(self, ctx:MiniGoParser.Assign_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs_assign.
    def visitLhs_assign(self, ctx:MiniGoParser.Lhs_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign.
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stms.
    def visitIf_stms(self, ctx:MiniGoParser.If_stmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifelse.
    def visitIfelse(self, ctx:MiniGoParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#or_expr.
    def visitOr_expr(self, ctx:MiniGoParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#and_expr.
    def visitAnd_expr(self, ctx:MiniGoParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logic_expr.
    def visitLogic_expr(self, ctx:MiniGoParser.Logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compare.
    def visitCompare(self, ctx:MiniGoParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#add_expr.
    def visitAdd_expr(self, ctx:MiniGoParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mul_expr.
    def visitMul_expr(self, ctx:MiniGoParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#neg_expr.
    def visitNeg_expr(self, ctx:MiniGoParser.Neg_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element_expr.
    def visitElement_expr(self, ctx:MiniGoParser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_expr.
    def visitStruct_expr(self, ctx:MiniGoParser.Struct_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#factor_expr.
    def visitFactor_expr(self, ctx:MiniGoParser.Factor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access_struct.
    def visitAccess_struct(self, ctx:MiniGoParser.Access_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_element.
    def visitMethod_element(self, ctx:MiniGoParser.Method_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#access_field.
    def visitAccess_field(self, ctx:MiniGoParser.Access_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_op.
    def visitMethod_op(self, ctx:MiniGoParser.Method_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index_op.
    def visitIndex_op(self, ctx:MiniGoParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funccall.
    def visitFunccall(self, ctx:MiniGoParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedecl.
    def visitTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_stuct.
    def visitType_stuct(self, ctx:MiniGoParser.Type_stuctContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_inter.
    def visitType_inter(self, ctx:MiniGoParser.Type_interContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#body_inter.
    def visitBody_inter(self, ctx:MiniGoParser.Body_interContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parammethod_op.
    def visitParammethod_op(self, ctx:MiniGoParser.Parammethod_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parammethod.
    def visitParammethod(self, ctx:MiniGoParser.ParammethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#body_type.
    def visitBody_type(self, ctx:MiniGoParser.Body_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#body_body_type.
    def visitBody_body_type(self, ctx:MiniGoParser.Body_body_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_array.
    def visitLiteral_array(self, ctx:MiniGoParser.Literal_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#space_array.
    def visitSpace_array(self, ctx:MiniGoParser.Space_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#space_array_op.
    def visitSpace_array_op(self, ctx:MiniGoParser.Space_array_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array.
    def visitArray(self, ctx:MiniGoParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_nested.
    def visitArray_nested(self, ctx:MiniGoParser.Array_nestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_list.
    def visitArray_list(self, ctx:MiniGoParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_param.
    def visitStruct_param(self, ctx:MiniGoParser.Struct_paramContext):
        return self.visitChildren(ctx)



del MiniGoParser