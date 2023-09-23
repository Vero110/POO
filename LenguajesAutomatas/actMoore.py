def findMajorityElement(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    return -1

if __name__ == '__main__':
    num_data = int(input("Cuantos datos desea ingresar? "))
    
    data_input = input(f"Por favor, ingrese {num_data} datos separados por comas: ")
    nums = list(map(int, data_input.split(',')))

    if len(nums) != num_data:
        print(f"Ha ingresado {len(nums)} datos, pero se esperaban {num_data} datos.")
    else:
        result = findMajorityElement(nums)

        if result != -1:
            print('El elemento mayoritario es:', result)
        else:
            print('El elemento mayoritario no existe')