from RemoteControl import RemoteControl

# Instanziierung

rc1 = RemoteControl(10)
print(f"{rc1.volume=}")

rc2 = RemoteControl(20)
print(f"{rc2.volume=}")
print(f"{rc2.programs[0]=}")


for i in range(0,10):
    rc1.plus()
print(f"{rc1.volume=}")

rc2.minus()
rc2.minus()
rc2.minus()
print(f"{rc2.volume=}")


print(f"{rc2.program[0]=}")

