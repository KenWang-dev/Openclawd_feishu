# GoF 设计模式横向（共时性）信息收集笔记

> 收集时间：2026-06-01
> 收集者：子Agent hv-gof-crosssectional

---

## 一、GoF 模式的现状（2024-2026）

### 1.1 总体概况

GoF（Gang of Four）的《Design Patterns: Elements of Reusable Object-Oriented Software》出版于1994年，距今已超过30年。在2025年的语境下，社区共识是：

- **模式本身的精神（intent）依然有价值，但具体代码实现已大量过时**
- **"Patterns are timeless. Their code is not."** — 这句话成为2025年最被广泛引用的总结
- 来源：https://medium.com/@freddy.dordoni/the-gang-of-four-gave-us-23-design-patterns-are-they-still-relevant-in-2025-f2e999c384c0

### 1.2 各模式在各语言中的实践状态

#### Java
- **仍大量使用**：Strategy、Observer、Factory、Builder、Singleton、Decorator、Proxy
- **Spring框架内建了大量GoF模式的实现**（如Proxy → Spring AOP, Observer → ApplicationEvent）
- **2025年趋势**：许多模式被 Java 新特性（Records, Sealed Classes, Pattern Matching）简化
  - Singleton → 枚举或 `record` 即可
  - Builder → Java 14+ Record 简化
  - Iterator → `for-each` 循环内建
- **"Design Patterns are Dead" 论**：2025年7月Medium文章直言"Gang of Four? More like Gang of Bloat"，认为现代Java特性让很多模式成为多余
  - 来源：https://medium.com/javaguides/design-patterns-are-dead-use-this-instead-in-modern-java-22770e4677e3

#### C#
- 与Java类似，GoF模式在.NET生态中根深蒂固
- ASP.NET Core 框架大量使用 Dependency Injection（基于 Factory + Singleton）
- LINQ 内建了 Iterator、Visitor 等模式
- 现代C#的泛型、委托、模式匹配也简化了很多GoF模式

#### Python
- **设计模式在Python中通常更简单**：Python的动态特性（鸭子类型、一等函数、装饰器语法糖）让许多GoF模式变得"隐形"
- Singleton → 模块天然就是单例
- Iterator → 内建的 `for x in iterable`
- Observer → 可用函数式回调代替
- Factory → 简单函数即可，无需类层次
- Strategy → 传入不同函数（lambda）
- Python社区对GoF模式的关注度较低，更倾向于"Pythonic"写法

#### Go
- **Go有意避开经典OOP**：没有继承、没有类，只有struct + 组合
- Refactoring.Guru 专门提供了 Go 语言的设计模式示例
  - 来源：https://refactoring.guru/design-patterns/go
- Go中常用的GoF模式（以组合和接口实现）：
  - Factory、Strategy、Observer、Singleton、Proxy
- Go社区更推崇 **"组合优于继承"**，很多模式需要重新设计实现方式

#### Rust
- **Rust彻底改变了GoF模式的实现方式**：没有传统OOP继承，所有权系统引入全新约束
- 2025年6月文章 "From GoF to Rustacean" 详细阐述了每个GoF模式在Rust中的"翻译"：
  - Singleton → `OnceCell` / `LazyLock`
  - Builder → Rust 的 `::new()` + 链式方法 + `Option` 字段
  - Strategy → 泛型 trait + impl
  - Observer → trait 回调或 channel
  - Factory → 关联函数 `::new()`
  - 来源：https://medium.com/@theopinionateddev/from-gof-to-rustacean-translating-classic-design-patterns-to-idiomatic-rust-36e62735e1eb
- Rust Unofficial Design Patterns 网站活跃更新：
  - 来源：https://rust-unofficial.github.io/patterns/
- GitHub上有专门仓库：https://github.com/fadeevab/design-patterns-rust

#### TypeScript/JavaScript
- **前端世界中GoF模式被框架内化**：
  - Observer → React `useEffect`, Vue `watch`
  - Strategy → 传入不同回调函数
  - Iterator → `for...of` / `Array.prototype.forEach`
  - Singleton → ES Module 天然单例
  - Template Method → 高阶函数
  - Decorator → React HOC（但已被Hooks取代）、TypeScript装饰器
  - Factory → 简单工厂函数
- 2025年文章指出：**"GoF patterns are sometimes overkill… a sign you're thinking in classes where you could think in functions"**
  - 来源：https://medium.com/@freddy.dordoni/the-gang-of-four-gave-us-23-design-patterns-are-they-still-relevant-in-2025-f2e999c384c0

### 1.3 仍然高价值的GoF模式（跨语言通用）
1. **Strategy** — 行为封装，几乎所有语言都频繁使用
2. **Observer / Pub-Sub** — 事件驱动核心，内建于几乎所有框架
3. **Factory / Abstract Factory** — 对象创建抽象，Spring/DI等框架基础
4. **Decorator** — 中间件、装饰器模式无处不在
5. **Builder** — 复杂对象构建仍需要
6. **Proxy** — AOP、网络代理、懒加载
7. **Facade** — API封装、子系统简化

### 1.4 已基本被语言特性淘汰的模式
1. **Iterator** — 几乎所有现代语言内建
2. **Singleton** — 模块/enum/静态常量即可
3. **Template Method** — 高阶函数/函数组合替代
4. **Command** — 一等函数即可，无需Command对象

---

## 二、替代方案/竞品模式体系

### 2.1 Enterprise Integration Patterns (EIP)
- **作者**：Gregor Hohpe, Bobby Woolf（2003年）
- **领域**：消息中间件、系统间集成
- **核心**：65种模式，覆盖消息通道、消息路由、消息转换、消息端点等
- **现状（2025）**：仍然高度相关
  - Kafka、RabbitMQ、AWS SNS/SQS 等消息系统的设计都基于EIP
  - Apache Camel 直接以EIP为编程模型
  - 来源：https://martinfowler.com/books/eip.html
- **与GoF的区别**：GoF面向对象内设计，EIP面向分布式系统集成

### 2.2 Patterns of Enterprise Application Architecture (PoEAA)
- **作者**：Martin Fowler（2002年）
- **核心模式**：Repository、Unit of Work、Data Mapper、Active Record、Service Layer、Transaction Script 等
- **现状（2025）**：
  - Repository Pattern 在 Java/C# 后端开发中仍是标配
  - Data Mapper → ORM（Hibernate, Entity Framework）的基石
  - Active Record → Ruby on Rails / Laravel 内建
  - 被awesome-software-design列为"仍然高度相关"的经典
  - 来源：https://martinfowler.com/articles/enterprisePatterns.html
- **与GoF的区别**：从"对象怎么协作"上升到"应用架构怎么组织"

### 2.3 微服务设计模式（Chris Richardson）
- **作者**：Chris Richardson，《Microservices Patterns》（2018年）
- **核心模式**：Decomposition、API Gateway、Service Discovery、Circuit Breaker、Saga、CQRS、Event Sourcing、Strangler Fig 等
- **现状（2025）**：极其活跃
  - 微服务架构已成为企业级默认选择
  - Kubernetes生态大量实践这些模式
  - 来源：https://microservices.io/patterns/
- **与GoF的区别**：GoF是对象级别模式，微服务模式是系统/架构级别

### 2.4 函数式编程模式
- **核心观点**：GoF的很多模式在FP中"隐形"或"简化"
- **Peter Norvig 的经典论证**：23种GoF模式中有**16种在Lisp/Dylan中"隐形或更简单"**
  - 来源：https://stackoverflow.com/questions/327955/does-functional-programming-replace-gof-design-patterns
- **Scott Wlaschin 的 FP Patterns**（F#为重点）：
  - 函数组合（Composition）
  - 柯里化（Currying）
  - Monad / Applicative Functor
  - 代数数据类型（ADT）
  - 部分应用（Partial Application）
  - 来源：https://www.reddit.com/r/programming/comments/61kt36/functional_programming_design_patterns_by_scott/
- **2025年 DEV.to 文章**逐个分析了23种GoF模式在FP中的替代：
  - Abstract Factory → 多态类型 + 类型类（Haskell）/ Tagless Final（Scala）
  - Factory Method → 简单构造函数
  - Strategy → 函数参数
  - Observer → FRP（函数式响应式编程）
  - 来源：https://dev.to/zelenya/functional-takes-on-gof-design-patterns-4jff
- **与GoF的区别**：FP模式以"函数组合"和"类型系统"为核心，而非"对象继承"

### 2.5 Clean Architecture / Hexagonal Architecture
- **核心人物**：Robert C. Martin (Uncle Bob)、Alistair Cockburn
- **Hexagonal Architecture（2005, Cockburn）**：
  - 核心理念：将业务逻辑置于中心，输入/输出通过"端口"和"适配器"连接
  - "Ports and Adapters" = 业务逻辑不依赖具体框架/数据库/UI
  - 来源：https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)
- **Clean Architecture（2017, Uncle Bob）**：
  - 依赖规则：外层依赖内层，永不反向
  - Entity → Use Case → Interface Adapter → Frameworks & Drivers
- **2025-2026年热度**：
  - 大量教程和指南持续发布（Java、.NET、TypeScript）
  - 与DDD（Domain-Driven Design）深度结合
  - 来源：https://medium.com/@ignatovich.dm/understanding-software-architecture-ddd-clean-architecture-and-hexagonal-architecture-13758e59c951
- **与GoF的区别**：从代码级别的"模式"上升到架构级别的"分层策略"

### 2.6 前端框架自带的设计模式
- **React 核心模式**（2025年）：
  - Hooks模式（useState, useEffect, useContext, useReducer）
  - Render Props → 已被Hooks取代
  - HOC（高阶组件）→ Decorator模式的前端版，已逐渐衰退
  - Compound Components（组合组件）
  - Custom Hooks（自定义Hook）→ 策略模式的函数式实现
  - Provider/Context → 全局状态管理
  - 来源：https://www.uxpin.com/studio/blog/react-design-patterns/
  - 来源：https://www.telerik.com/blogs/react-design-patterns-best-practices
- **Vue 核心模式**（2025年）：
  - Composition API → 函数式逻辑复用
  - Provide/Inject → 依赖注入
  - Smart vs Dumb Components → 职责分离
  - Slots → 内容分发模式
  - 来源：https://vueschool.io/articles/vuejs-tutorials/5-component-design-patterns-to-boost-your-vue-js-applications/
- **2025年讨论**：React Hooks模式甚至开始影响后端设计（替代OO监听器模式）
  - 来源：https://www.reddit.com/r/reactjs/comments/1p7uw6q/beyond_the_frontend_how_the_react_hooks_pattern/
- **与GoF的区别**：前端框架模式是**框架特定的**、数据驱动的、声明式的，而非通用的OOP模式

### 2.7 云原生设计模式
- **Kubernetes Patterns**（Bilgin Ibryam, Roland Huss, O'Reilly）：
  - 第二版于2023年出版
  - 核心模式类别：
    - **基础模式**：ConfigMap, Secret, Sidecar
    - **结构性模式**：Ambassador, Adapter, Scatter/Gather
    - **行为模式**：Health Probe, Scheduled Action, Worker Queue
    - **高可用模式**：Bulkhead, Circuit Breaker, Leader Election
    - **网络模式**：Service Mesh, Ingress Controller
  - 来源：https://www.oreilly.com/library/view/kubernetes-patterns-2nd/9781098131678/
- **2025年云原生架构模式**：
  - Microservices + Containerization + Service Mesh + Observability + CI/CD + Serverless + Event-Driven
  - 来源：https://blog.madrigan.com/blog/202511271647/
  - CNCF Survey 2024：Kubernetes高级部署提升55%的部署效率
- **2026年云原生设计模式指南**：
  - 10大核心类型：基础设施即代码、服务网格、事件驱动、CQRS、Saga、Sidecar、Ambassador、Adapter、Strangler、Circuit Breaker
  - 来源：https://clearfuze.com/blog/cloud-native-architecture-patterns/
- **与GoF的区别**：云原生模式关注**分布式系统**层面的部署、通信、容错，而非对象间协作

---

## 三、各竞品与GoF的核心方法论差异

| 维度 | GoF模式 | 微服务模式 | FP模式 | 云原生模式 | 前端框架模式 |
|------|---------|-----------|--------|-----------|-------------|
| **关注层次** | 对象/类级别 | 系统/服务级别 | 函数/类型级别 | 基础设施级别 | 组件/UI级别 |
| **核心思维** | 继承+多态 | 分布式+解耦 | 纯函数+组合 | 容器+编排 | 声明式+数据流 |
| **解决的核心问题** | 对象如何协作 | 服务如何通信/部署 | 状态如何管理 | 系统如何弹性运行 | UI如何响应数据变化 |
| **变化的原因** | 需求变化 | 业务规模变化 | 数据流变化 | 运行时环境变化 | 用户交互变化 |
| **测试单元** | 类/对象 | 服务/接口 | 纯函数 | Pod/容器 | 组件/页面 |

---

## 四、用户口碑与社区讨论

### 4.1 GitHub 数据

| 仓库 | Stars | 说明 |
|------|-------|------|
| DovAmir/awesome-design-patterns | **47.5k** ★ | 最全面的设计模式合集（含GoF和现代模式）|
| RefactoringGuru/design-patterns-java | ~1.1k ★ | Refactoring.Guru的Java设计模式示例 |
| RefactoringGuru/design-patterns-php | ~1.1k ★ | PHP版 |
| RefactoringGuru/design-patterns-cpp | ~382 ★ | C++版 |
| fadeevab/design-patterns-rust | 活跃更新 | Rust版GoF 23种模式 |
| rust-unofficial.github.io/patterns | 活跃更新 | Rust非官方设计模式（非GoF） |
| GitHub Topics: design-patterns | 22.2k+ ★ 仓库 | 设计模式标签下最热门仓库 |
| DesignPatternsPHP (domnikl) | 22.2k ★ | PHP 8.x 设计模式示例 |

**来源**：https://github.com/topics/design-patterns, https://github.com/DovAmir/awesome-design-patterns

### 4.2 refactoring.guru
- 全球排名约 53,370-62,833（SimilarWeb数据）
- 多语言版本（英语、中文、西班牙语等）活跃维护
- 中文版（refactoringguru.cn）在中国开发者中广泛使用
- 来源：https://refactoring.guru/

### 4.3 Hacker News 讨论（关键帖子）

#### "Are design patterns still a thing?" (2019年11月)
- **主流观点**：设计模式无处不在，只是"隐形"了
- "每个你用 `foreach` 的时候，你都在用 Iterator 模式"
- "SOLID 原则比 GoF 模式更值得今天学习"
- 来源：https://news.ycombinator.com/item?id=21645883

#### "Design patterns feel completely obsolete now" (2018年2月)
- "大多数设计模式是有害的，现在由于函数式语言特性已完全不需要"
- "设计模式就像TDD，没人想承认，但它们真的..."
- 来源：https://news.ycombinator.com/item?id=16351750

#### "I'm Sick Of GOF Design Patterns" (2014年8月)
- 讨论了面试中过度强调GoF模式的问题
- 来源：https://news.ycombinator.com/item?id=8103496

#### "Design Patterns Are Temporary, Language Features Are Forever" (2024年9月)
- 核心论点：设计模式是对语言缺陷的补丁，语言进化后模式自然消亡
- Reddit镜像：https://www.reddit.com/r/hackernews/comments/1fcxcrx/

### 4.4 Reddit 讨论

#### r/programming "Are design patterns still relevant?" (2020年12月)
- "它们确实提供了简化讨论的命名，但从未解决'何时使用什么'的问题"
- 来源：https://www.reddit.com/r/programming/comments/kn1ltc/

#### r/reactjs "Beyond the Frontend: React Hooks Pattern" (2025年11月)
- React Hooks模式开始反哺后端设计，替代OO监听器模式
- 来源：https://www.reddit.com/r/reactjs/comments/1p7uw6q/

### 4.5 知乎讨论

#### "GOF设计模式过时了吗？" (2022年11月)
- 知友共识：**不必生搬硬套，理解思想比死记硬背更重要**
- "保持初心——提升代码的可读性、可扩展性、可维护性"
- 来源：https://www.zhihu.com/question/564066313

#### "设计模式学习方法？" (经典帖)
- "GoF从大量代码实践中总结了一套方法论，而新人可能连代码都写得少"
- 来源：https://www.zhihu.com/question/33651897

#### 2026年Java学习路线
- "设计模式是初中级程序员迈向高级程序员的必经之路"
- 来源：https://javabetter.cn/xuexiluxian/java/yitiaolong.html

#### "2026年程序员不要再学这些技术了！"
- 暗示设计模式已不在"必学新技术"列表中
- 来源：https://zhuanlan.zhihu.com/p/2011858741637690648

---

## 五、争议与批评

### 5.1 "设计模式已死"论

**核心论据**：
1. **语言进化论**：现代语言（Java 8+, Kotlin, Rust, TypeScript）的函数式特性让很多GoF模式成为多余
2. **框架内化论**：Spring、React、Kubernetes等框架已将设计模式"内建"，开发者无需手动实现
3. **AI替代论**：2026年GitHub Copilot可生成46%的代码，AI能自动识别和应用设计模式

**代表文章**：
- "💀 Design Patterns are Dead. Use This Instead in Modern Java" (2025年7月)
  - https://medium.com/javaguides/design-patterns-are-dead-use-this-instead-in-modern-java-22770e4677e3
- Adam Bien（Java Champion）："With Java EE 7, Design Patterns are dead"
  - https://www.theserverside.com/tip/With-Java-EE-7-your-Design-Patterns-are-dead-And-your-EAR-is-ugly-too

### 5.2 "设计模式永恒"论

**核心论据**：
1. **共享语言论**：设计模式的价值在于提供了**共同词汇**，而非代码模板
   - "Ok team! Let's refactor this into a Strategy pattern." — 无需解释意图
2. **面试刚需论**：系统设计面试、架构评审仍频繁使用设计模式术语
3. **Legacy代码论**：大量企业级Java/C#/C++代码仍重度使用GoF模式
4. **精神永恒论**：模式背后的设计意图（解耦、封装变化点、单一职责）永远有价值

**代表观点**：
- "Patterns are timeless. Their code is not."
  - https://medium.com/@freddy.dordoni/the-gang-of-four-gave-us-23-design-patterns-are-they-still-relevant-in-2025-f2e999c384c0
- "在面试中，设计模式仍出现" — 同上

### 5.3 Peter Norvig 的经典批评

- **原话**："16 of the 23 patterns in Design Patterns were 'invisible or simpler' in Lisp/Dylan"
- **演讲**：2004年 LL2 会议，"Design Patterns in Dynamic Languages"
  - 来源：http://www.norvig.com/design-patterns/
- **HN名句**："As Peter Norvig famously said, 'Design patterns are bug reports against your programming language'"
  - 来源：https://news.ycombinator.com/item?id=8735187
- **社区延伸解读**："设计模式是对编程语言缺陷的bug报告"
  - 来源：https://www.reddit.com/r/hackernews/comments/1fcxcrx/

### 5.4 Sandi Metz 的重新解读

- **代表著作**：《Practical Object-Oriented Design in Ruby》(POODR, 2012)
  - 官网：https://www.poodr.com/
- **核心主张**：
  - 不死记硬背GoF模式名，而是**理解设计原则（SOLID、DRY、YAGNI）**
  - 设计模式是**自然涌现**的，当你理解了设计原则后会自然使用
  - Template Method、Strategy等模式在POODR中从"解决问题的方案"变为"良好设计的自然结果"
  - 来源：https://www.endpointdev.com/blog/2024/02/key-takeaways-from-poodr/
- **其他著作**：《99 Bottles of OOP》（与Katrina Owen合著）
- **2024-2025年**：POODR课程仍在Sandi Metz官网销售，设有Peer Group学习机制
  - 来源：https://sandimetz.com/courses
- **社区评价**：Reddit r/ruby 社区在2023年仍有 "POODR Still Worth Reading?" 的讨论，结论是**强烈推荐**
  - 来源：https://www.reddit.com/r/ruby/comments/16s62eo/

### 5.5 "设计模式是语言bug报告"论

- 这个观点在HN和Reddit上广泛传播
- 核心逻辑：如果一门语言需要设计模式来解决某个问题，说明语言本身缺乏解决这个问题的能力
- 随着语言进化，这些"bug"被修复，设计模式自然消亡
- 反对观点：并非所有模式都能被语言特性替代（如架构级别的模式）

---

## 六、生态位分析（2026年的定位）

### 6.1 GoF 模式在2026年的定位

**1. 从"实现指南"到"共享语言"**
- GoF模式的价值已从**代码模板**转变为**沟通工具**
- 2025-2026年的共识：不需要手写每个模式的经典实现，但需要理解模式名称代表的**意图和权衡**

**2. 从"解决方案"到"设计原则的实例"**
- Sandi Metz路线已成为主流：理解SOLID原则 → 自然产生模式
- 设计模式不再是需要"记忆和应用"的23个配方，而是良好OOP设计的**自然结果**

**3. 从"OOP专属"到"跨范式"**
- GoF模式的**精神**在函数式编程、前端开发、云原生架构中都有体现
- 只是实现方式完全不同：从"类+继承"变为"函数+组合"或"服务+消息"

**4. 被"分层碾压"**
```
           架构级模式（DDD, Clean Arch, Hexagonal）
           /          \          \
       微服务模式    前端框架模式    云原生模式
          /            \             \
       GoF模式 ← 被"内化"到这些层次中
          \
       函数式模式（替代部分GoF模式）
```

### 6.2 关键趋势

1. **设计模式的"下沉"**：从显式编码变为隐式框架特性
   - GoF模式 → Spring Framework 功能
   - GoF模式 → React Hooks / Vue Composition API
   - GoF模式 → Kubernetes Operator

2. **AI对设计模式的影响**：
   - AI能自动识别和应用设计模式（GitHub Copilot生成46%代码）
   - 但也导致代码克隆增加4倍（GitClear 2025数据）
   - 人类开发者更需要**理解设计原则**来判断AI生成代码的质量
   - 来源：https://www.gitclear.com/ai_assistant_code_quality_2025_research

3. **面试/教育中的定位变化**：
   - Java面试仍将设计模式作为必考题（尤其中国/印度市场）
   - 但考察重点从"手写实现"变为"理解意图和场景应用"
   - 知乎/CSDN 仍有大量"2025设计模式面试题"

4. **中国开发者社区的独特视角**：
   - 知乎上对"GoF设计模式过时了吗"的回答：**理解思想，不套公式**
   - CSDN 2024年仍将设计模式列为Java面试核心
   - 但2026年知乎文章"程序员不要再学这些技术了"暗示设计模式不在推荐列表

### 6.3 GoF 模式在 2026 年的最终定位总结

| 维度 | 定位 |
|------|------|
| **代码编写** | 大部分已被语言/框架内化，手动实现需求降低 |
| **沟通工具** | 仍然是最通用的设计沟通词汇之一 |
| **教育/面试** | Java/C#生态中仍是核心考点 |
| **架构决策** | 精神层面仍有价值，但被更高层次的架构模式覆盖 |
| **新兴范式** | FP/前端/云原生有自己的模式体系，但部分GoF精神可移植 |
| **AI时代** | 理解设计模式思想仍是判断AI代码质量的关键能力 |

---

## 七、信息来源汇总

### 关键文章
1. "The Gang of Four Gave Us 23 Design Patterns… Are They Still Relevant in 2025?" — https://medium.com/@freddy.dordoni/the-gang-of-four-gave-us-23-design-patterns-are-they-still-relevant-in-2025-f2e999c384c0
2. "Design Patterns are Dead. Use This Instead in Modern Java" — https://medium.com/javaguides/design-patterns-are-dead-use-this-instead-in-modern-java-22770e4677e3
3. "Functional Takes on GoF Design Patterns" — https://dev.to/zelenya/functional-takes-on-gof-design-patterns-4jff
4. "From GoF to Rustacean" — https://medium.com/@theopinionateddev/from-gof-to-rustacean-translating-classic-design-patterns-to-idiomatic-rust-36e62735e1eb
5. "Design Patterns: The Complete Guide 2025" — https://www.technologyandstrategy.com/news/design-patterns-the-complete-guide-2025

### Hacker News 讨论
1. "Ask HN: Are design patterns still a thing?" — https://news.ycombinator.com/item?id=21645883
2. "Design patterns feel completely obsolete now" — https://news.ycombinator.com/item?id=16351750
3. "I'm Sick Of GOF Design Patterns" — https://news.ycombinator.com/item?id=8103496
4. "Design Patterns Are Temporary, Language Features Are Forever" — https://www.reddit.com/r/hackernews/comments/1fcxcrx/

### Stack Overflow / Stack Exchange
1. "Does functional programming replace GoF design patterns?" — https://stackoverflow.com/questions/327955/
2. "Where are all the functional programming design patterns?" — https://softwareengineering.stackexchange.com/questions/89273/

### 参考网站
1. Refactoring.Guru — https://refactoring.guru/design-patterns/catalog
2. Microservices.io Patterns — https://microservices.io/patterns/
3. Martin Fowler - Patterns in Enterprise Software — https://martinfowler.com/articles/enterprisePatterns.html
4. Rust Unofficial Design Patterns — https://rust-unofficial.github.io/patterns/
5. Sandi Metz / POODR — https://www.poodr.com/ / https://sandimetz.com/

### GitHub
1. DovAmir/awesome-design-patterns (47.5k★) — https://github.com/DovAmir/awesome-design-patterns
2. fadeevab/design-patterns-rust — https://github.com/fadeevab/design-patterns-rust
3. RefactoringGuru org — https://github.com/RefactoringGuru

### 知乎
1. "GOF设计模式过时了吗？" — https://www.zhihu.com/question/564066313
2. "设计模式学习方法？" — https://www.zhihu.com/question/33651897

### AI 与代码质量
1. GitClear: AI Copilot Code Quality 2025 — https://www.gitclear.com/ai_assistant_code_quality_2025_research
2. "AI Is Writing 46% of All Code" — https://medium.com/@reliabledataengineering/ai-is-writing-46-of-all-code-github-copilots-real-impact-on-15-million-developers-787d789fcfdc

### 云原生
1. Kubernetes Patterns, 2nd Ed (O'Reilly) — https://www.oreilly.com/library/view/kubernetes-patterns-2nd/9781098131678/
2. "Cloud-Native Architecture Patterns for 2025" — https://medium.com/@reiqwan/cloud-native-architecture-patterns-for-2025-building-enterprise-systems-that-scale-7c465142aaa4
3. "Cloud Native Design Patterns 2026 Guide" — https://clearfuze.com/blog/cloud-native-architecture-patterns/
