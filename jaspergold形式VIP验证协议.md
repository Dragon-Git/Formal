# 使用jaspergold形式VIP验证协议

## cadence 形式 VIP 协议

- AMBA 总线
  - AHB and APB
  - AXI
  - ACE-SYS
  - ATB
  - CHI
- 存储器
  - DDR
  - LPDDR
  - SDRAM
- PHY
  - DFI
  - PIPE（PCI Express® 的 Phy 接口）
- 其他
  - SPI
  - IIC
  - OCP

具体请参考[cadence官网](https://www.cadence.com/zh_CN/home/tools/system-design-and-verification/verification-ip/formal-vip.html)

## 步骤

需要提前准备好待验ip的dut

- 1.使用jaspergold打开vip，会在work目录生成checker和tcl脚本
```bash
jg -pk abvip.jdb &
```
- 2.根据duv和生成的checker，编写bind文件，bind 语法为：
```systemverilog
bind dut_module_name checker_module_name checker_instance_name(.chk_port(dut_port))
```
- 3.修改tcl脚本中的相应参数，必须修改的有dut文件和待测路径，并在最后添加
```tcl
prove -all
```
- 4.在jg中执行tcl文件
