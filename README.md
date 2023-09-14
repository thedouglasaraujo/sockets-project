<h1 align="center">Programação com Sockets - Aplicação cliente-servidor 🧮</h1>

## :memo: Descrição
O serviço desenvolvido é uma calculadora remota com base em uma aplicação cliente-servidor simples, implementada em Python com a utilização de sockets. A calculadora remota permite que clientes enviem expressões matemáticas para um servidor, que então realiza os cálculos e retorna os resultados aos clientes. O projeto é dividido em três partes principais: um servidor DNS para registro, consulta e remoção de serviços, um servidor TCP para comunicação confiável e um servidor UDP para comunicação de alta velocidade. Os clientes consultam o servidor DNS para obter o IP e a porta do serviço da calculadora remota e realizam cálculos matemáticos, registrando tempos de execução para análise comparativa.

## :wrench: Tecnologias utilizadas
- Python
- Socket
- Threading
- Signal
  
## 	:arrow_forward: Executar o projeto
- Tendo o Python 3 instalado na máquina, basta baixar este repositório por zip ou pelo git clone.
- A ordem de execução é: DNS -> Servidores -> Clientes.
- Você pode executar os dois pares (clientes e servidores) do UDP e TCP ao mesmo tempo ou executar apenas um par de uma das duas comunicações.
- Lembrando que cada um dos arquivos deve ser rodado em terminais diferentes.

## :camera: Capturas
[Clique aqui para acessar as capturas realizadas no Wireshark](https://github.com/thedouglasaraujo/sockets-project/blob/main/capturas-wireshark/README.md)
