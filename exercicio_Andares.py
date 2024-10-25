Solução : Com o loop for

for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)


Solução : Com o loop while

andar = 20

while andar > 0:
    if andar != 13:
        print(andar)
    andar -= 1


Solução :  No python não tem o loop do-while, vou usar while true e uma verificação de condição para quebrar o loop.

andar = 20
while True:
    if andar != 13:
        print(andar)
    andar -= 1
    if andar == 0:
        break

O loop do-while em Java-cript :

let andar = 20;

do {
  if (andar !== 13) {
    console.log(andar);
  }
  andar--;
} while (andar > 0);

