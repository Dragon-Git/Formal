# 形式验证

## 目录

- [前言](#前言)
- [SLINT](#SLINT)
- [FPV](#FPV)
- [XPV](#XPV)

## 前言

基于形式化的验证流程。 数字 IP 已使用此方法进行完全的验证， 并且 sign-off（形式化 sign-off)。 该流程基于形式化应用程序的使用和 SVA 代码的开发， 以验证该模块的所有功能。
常见的形式化流程为： 
- 使用静态语法检查清理 RTL 代码
- CDC/RDC 检查
- ABVIP（基于断言的验证IP）验证总线协议 一 例 如 AMBA(advanced micro controller bus architecture) 总线
- 控制和状态寄存器验证 
- 形式属性验证（功能特征验证） 
- 代码和功能覆盖率提取 
- 通过证明新的SVA 断言来优化覆盖范围 
## SLINT 
全称super lint， 
## FPV 
全称(Formal Property Verification) 
## XPV 
全称(X-Propagation Verification) 
## CONN 
全称(Connectivity Verification App) 
## AMA 
全称(Architectural Modeling App)  
jaspergold app 命令为```jg -arch```
## CSR 
全称(Control and Status Register))  
```jg -csr```
## RTLD 
全称(RTL Development App)  
```jg -rtld```
## ESA 
全称(Executable Specification App)  
```jg -spec```
## BPS 
全称(Behavioral Property Synthesis)  
```jg -bps```
## SPS 
全称(Structural Property Synthesis)  
```jg -sps```
## LPV 
全称(Low Power Verification) 
## SEC 
全称(Sequential Equivalence Checking)  
```jg -sec```
## SPV 
全称(Security Path Verification)  
```jg -spv```
## CA 
全称(Coverage App)  
```jg -cov```
