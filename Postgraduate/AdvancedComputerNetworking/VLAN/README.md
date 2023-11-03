# VLAN间单臂路由配置

## Step 1

请严格按照以下顺序执行：

1. 拖入R1、R2（c3600）

2. 拖入PC1、PC2（注意此时不要连线、不要启动节点）

3. 按照题目要求配置R2（添加slots、更改图标，不要更改hostname）

4. 运行所有节点，右上角所有节点前亮绿灯即为成功运行

5. 双击R2打开控制台，按照题目要求关闭路由功能，而后保存配置

   ```
   R2#conf t
   R2(config)#no ip routing
   R2(config)#end
   R2#write
   ```

6. 关闭所有节点，按题目要求将R2的hostname更改为SW1
7. 按题目要求连接所有拓扑，并开启设备
8. Tools$\to$Import/Export Node Configs 保存配置文件

