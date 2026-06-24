import subprocess

def ejecutar_comando(comando):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return resultado.stdout.strip()

def cifrado_cesar(char, shift):
    if char.isalpha():
        char = char.upper()
        inicio = ord('A')
        return chr((ord(char) - inicio + shift) % 26 + inicio)
    return char

def main():
    log = ejecutar_comando('git log --reverse --format="%H|%P"')
    llave = ""
    
    for linea in log.splitlines():
        if not linea: continue
        partes = linea.split('|')
        hash_c = partes[0]
        padres = partes[1] if len(partes) > 1 else ""
        
        # 4. Mutación Final: Inversión en Merge
        if len(padres.split()) > 1:
            llave = llave[::-1]
            
        # 1. Extracción: Verificamos si existe el archivo antes de procesar
        contenido = ejecutar_comando(f'git show {hash_c}:nucleo.txt')
        if not contenido:
            continue
        
        # 2. Evaluación de Estado
        valor_decimal = int(hash_c[:6], 16)
        cant_nums = sum(c.isdigit() for c in hash_c)
        cant_letras = sum(c in 'abcdefABCDEF' for c in hash_c)
        
        # 3. Máquina de Estados
        if valor_decimal % 2 == 0:
            llave += cifrado_cesar(contenido[0], cant_nums)
        else:
            llave += chr(ord(contenido[-1]) + cant_letras)
            
    print(f"La Llave final es: {llave}")

if __name__ == '__main__':
    main()