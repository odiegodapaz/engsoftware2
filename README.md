# engsoftware2
Design Patterns Adapter
Engenharia de Software II

Introdução ao Adapter
O padrão de projeto Adapter (adaptador) é um padrão estrutural que permite que objetos com interfaces incompatíveis trabalhem juntos. Ele é usado quando há a necessidade de fazer uma adaptação entre duas classes ou interfaces que possuem interfaces diferentes ou incompatíveis.
O Adapter atua como uma camada intermediária que converte a interface de um objeto em outra interface que o cliente espera. Isso permite que objetos com diferentes interfaces colaborem entre si, mesmo que inicialmente não fossem compatíveis.espera. Isso permite que objetos com diferentes interfaces colaborem entre si, mesmo que inicialmente não fossem compatíveis.

Analogia com o mundo real 
Quando você viaja do Brasil para a Europa pela primeira vez, você pode ter uma pequena surpresa quando tenta carregar seu laptop. O plugue e os padrões de tomadas são diferentes em diferentes países. É por isso que seu plugue do Brasil não vai caber em uma tomada da Alemanha. O problema pode ser resolvido usando um adaptador de tomada que tenha o estilo de tomada Brasileira e o plugue no estilo Europeu.

Principios
Alvo (Target): Define a interface específica que o cliente usa.
Adaptador (Adapter): É o objeto que adapta a interface existente do Adaptee para a interface esperada pelo cliente. Ele implementa a interface do Alvo e mantém uma referência para o Adaptee.
Adaptee: É a classe ou objeto existente que precisa ser adaptado. Ele possui uma interface incompatível com a interface do Alvo.

Sobre o processo de Adaptação
O processo de adaptação envolve o Adapter recebendo uma solicitação do cliente através do Alvo. O Adapter, por sua vez, realiza a tradução necessária para chamar os métodos adequados no Adapter, que executa a funcionalidade real. Em seguida, o Adapter retorna o resultado para o cliente através do Alvo.
O padrão Adapter é útil em situações em que você deseja reutilizar uma classe existente que não possui a interface necessária pelo cliente. Ele permite que você adicione adaptadores para conectar novas classes sem modificar o código existente.
Além disso, o Adapter também pode ser usado para envolver múltiplos objetos em um único objeto com uma interface unificada. Isso é conhecido como Adapter de objetos. Nesse caso, o Adapter contém instâncias dos objetos Adapters e os chama conforme necessário para atender às solicitações do cliente.

Prós e contras do Adapter

Prós
Princípio de responsabilidade. Você pode separar a conversão de interface ou dados da lógica primária do negócio do programa
Princípio aberto/fechado. Você pode introduzir novos tipos de adaptadores no programa sem quebrar o código cliente existente, desde que eles trabalhem com os adaptadores através da interface cliente.

Contras
A complexidade geral do código aumenta porque você precisa introduzir um conjunto de novas interfaces e classes. Algumas vezes é mais simples mudar a classe serviço para que ela se adeque com o resto do seu código

Algumas relações com outros padrões
O Adapter muda a interface de um objeto existente, enquanto que o Decorator melhora um objeto sem mudar sua interface. Além disso, o Decorator suporta composição recursiva, o que não seria possível quando você usa o Adapter.
O Adapter fornece uma interface diferente para um objeto encapsulado, o Proxy fornece a ele a mesma interface, e o Decorator fornece a ele com uma interface melhorada
O Bridge é geralmente definido com antecedência, permitindo que você desenvolva partes de uma aplicação independentemente umas das outras. Por outro lado, o Adapter é comumente usado em aplicações existentes para fazer com que classes incompatíveis trabalhem bem juntas.

Exemplos de uso
Exemplo sem o uso de Adapter:
Neste exemplo, temos três classes principais: PaymentService representa um serviço de pagamento, ShoppingCart representa um carrinho de compras e Item representa um item de compra. O carrinho de compras possui um método checkout que processa o pagamento usando um serviço de pagamento específico.
Observe que neste código não é necessário utilizar o padrão Adapter, pois as classes PaymentService e ShoppingCart têm uma interface direta e compatível. O carrinho de compras recebe uma instância do serviço de pagamento e chama o método process_payment diretamente.

Exemplos de uso
Exemplo sem o uso de Adapter:
Neste exemplo, temos três classes principais: PaymentService representa um serviço de pagamento, ShoppingCart representa um carrinho de compras e Item representa um item de compra. O carrinho de compras possui um método checkout que processa o pagamento usando um serviço de pagamento específico.
Observe que neste código não é necessário utilizar o padrão Adapter, pois as classes PaymentService e ShoppingCart têm uma interface direta e compatível. O carrinho de compras recebe uma instância do serviço de pagamento e chama o método process_payment diretamente.
continuação

Exemplos de uso
Exemplo Com uso de Adapter
Nesse caso, vamos criar um adaptador para permitir que o PaymentService seja compatível com a interface esperada pelo ShoppingCart.
Neste exemplo, adicionamos a classe PaymentAdapter, que implementa a mesma interface esperada pelo ShoppingCart através do método checkout. O adaptador recebe uma instância do PaymentService em seu construtor e, ao chamar o método checkout, repassa a chamada para o process_payment do serviço de pagamento.
Dessa forma, o carrinho de compras pode usar o adaptador de pagamento, que é compatível com sua interface, para processar o pagamento sem conhecer diretamente o PaymentService. Isso facilita a substituição do serviço de pagamento por outro no futuro, se necessário, mantendo a compatibilidade com a interface do carrinho de compras.

Exemplos de uso
Exemplo Com uso de Adapter
Nesse caso, vamos criar um adaptador para permitir que o PaymentService seja compatível com a interface esperada pelo ShoppingCart.
Neste exemplo, adicionamos a classe PaymentAdapter, que implementa a mesma interface esperada pelo ShoppingCart através do método checkout. O adaptador recebe uma instância do PaymentService em seu construtor e, ao chamar o método checkout, repassa a chamada para o process_payment do serviço de pagamento.
Dessa forma, o carrinho de compras pode usar o adaptador de pagamento, que é compatível com sua interface, para processar o pagamento sem conhecer diretamente o PaymentService. Isso facilita a substituição do serviço de pagamento por outro no futuro, se necessário, mantendo a compatibilidade com a interface do carrinho de compras.
continuação

Diego Da Paz, Otávio Mastrantonio e Roberto Lukas Pereira Diago
