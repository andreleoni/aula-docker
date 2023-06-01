COntainers estão mudando a forma que as coisas são desenvolvidas.

---

Como era antes de containers?

Utilização de VM, porém, VM é muito mais pesado, pois não compartilha o recurso computacional do computador.

Esta mudando a forma que a industria produz software, desde pequenas startups a grandes organizações

Containers são utilizados para encapsular dependências.

Resolve problemas do famoso "dependency hell"

Como uma VM, o container irá isolar a execução de um sistema operacional, que nós podemos utilizar para rodar aplicações.

Contudo, containers são muito mais vantajosos que VMS.

* Containers compartilham recursos com o sitema de maneira muito mais eficiente;
* são muito mais portáteis e ocupam menos espaço no sistema;
* são muito mais leve para os desenvolvedores que podem rodar dezenas de containers ao mesmo tempo, podendo simular sistemas produtivos com maior eficiência, e tirando a desculpa de "na minha máquina funciona"
& containres tembém ajudam desenvolvedores a ter sistemas mais parecidos com produção sem precisar gastar dezenas de horas configurando e instalando dependências nas máquinas.

---

Continers existem desde 1998, FreeBSD tem esta ferramenta de exteder o Chroot a processos. olaris ones ofereçan a solução de containerização completa apenas em 2001, mas foi limitada pois estava apenas nos ambientes Solaris OS.

Em 2001, Parallels

O projeto linux containers (LXC)  começou pelo Google em 2008e brotuhgh togeter CGroups , kernel, namespaces e CHroot para procer completa isolação do ambiente, em 2013, docker construiu as peças finais para resolver o quebra cabeça de containerização, e a tecnologia começou a ser comercializada no mainstream.

O docker comercializaou e popularizou o uso de containers entao, de uma maneira muito fácil.

Como o docker é opensource, começamos a ter um grande crescimento da comunidade
