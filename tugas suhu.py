# program untuk menghitung suhu
 
#celcius ke reamur
def conv_reamur(celcius):
    convert_reamur = 4 * celcius / 5
    return convert_reamur
    
#celcius ke kelvin
def conv_kelvin(celcius):
    convert_kelvin = celcius + 273
    return convert_kelvin 

#celcius to farenheit
def conv_farenheit(celcius):
    convert_farenheit = 9 * celcius / 5 + 32
    return convert_farenheit
 
#char utama
def main():
    print('Program Konversi Suhu')
    print('=======================')
 
    # create input
    temperature = int(input('Masukan Skala Celcius: '))
 
    # cetak hasil
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(f'Hasil Konnversi Suhu {temperature} C adalah {conv_reamur(temperature)} Reamur')
    print(f'Hasil Konversi Suhu {temperature} C adalah {conv_kelvin(temperature)} Kelvin')
    print(f'Hasil Konversi Suhu {temperature} C adalah {conv_farenheit(temperature)} Farenheit')
    print('++++++++++++++++++++++++++++++++++++++++++++')
 
if __name__=='__main__':
    main()