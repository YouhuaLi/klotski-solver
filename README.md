## 西游取真经游戏的求解器

原始游戏图片如下：

左上为“西游取真经”开局：
![](https://github.com/YouhuaLi/klotski-solver/blob/master/readme_images/quzhenjing_1.jpg?raw=true)

实物图
![](https://github.com/YouhuaLi/klotski-solver/blob/master/readme_images/quzhenjing_2.jpg?raw=true)

最难开局，理论最佳207步。因本程序每部只移动一个单位，所以输出为303个状态，共302步：

![https://github.com/YouhuaLi/klotski-solver/blob/master/readme_images/hardest_openning.png?raw=true]

## 运行例子：

枚举所有解，可能要运行6到10个小时：

Running it:

```
$ python main.py 
Finished in 113023.16320681572 seconds
  9094398 unique solutions
  303 moves in shortest solution
  375 moves in longest solution
  9094398 unique end states
  105644294 board configurations examined
  0 board configurations total (-105644294 unreachable)
```

## 生成动画：

依赖 [manim|https://docs.manim.community/en/stable/index.html]

在manim目录中：

```
manim -pql show_solution.py Show_Solution_QuZhenJing
manim -pql show_solution.py Show_Solution_Hardest
```
在 manim/sample_videos 目录中，有两个做好的动画

## 提示：

Hardcod的东西非常多，抱歉！