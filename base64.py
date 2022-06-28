import argparse
import logging
from encode import encode_ASCII
from decode import decode_base64

logging.basicConfig(filename='b64.log', encoding='utf-8', level=logging.DEBUG)

def get_source(string, filename):
    """
  :param string: string from -s arg
  :apram filename: link to file from -f arg
  :return: the content to decode/encode
  """
    if filename:
        # If a filename is provided, get his content
        with open(filename) as f:
            content = f.read()
            f.close()
            return content

    return string


parser = argparse.ArgumentParser()

encode_or_decode_group = parser.add_mutually_exclusive_group(required=True)
encode_or_decode_group.add_argument("-encode", help="Encodage d'une chaîne de caractères ASCII vers base 64",
                                    action="store_true")
encode_or_decode_group.add_argument("-decode", help="Décodage d'une chaîne de caractères Base 64 vers ASCII",
                                    action="store_true")

string_or_filename_group = parser.add_mutually_exclusive_group(required=True)
string_or_filename_group.add_argument("-s", "--string", help="Chaîne de caractères à encoder/décoder", action="store")
string_or_filename_group.add_argument("-f", "--filename", help="Chemin vers un fichier à encoder/décoder",
                                      action="store")

parser.add_argument("-o", "--output", help="Chemin vers le fichier de sortie")
parser.add_argument("-l", help="Niveau d'accés au log")
args = parser.parse_args()
print("arg.log")

# get the content to encode or decode from the -s/-f args
source = get_source(args.string, args.filename)

if args.encode:
    logging.info("Début encodage")
    logging.debug(f"Fichier source : {args.filename}" if args.filename else "Pas de fichier source")
    logging.debug(f"Encodage de la chaîne de caractères '{source}'")
    logging.debug(f"Fichier de sortie : {args.output}" if args.output else "Pas de fichier de sortie")

    # Encoding process
    encode_ASCII(source, args.output)

elif args.decode:
    logging.info("Début décodage")
    logging.debug(f"Fichier source : {args.filename}" if args.filename else "Pas de fichier source")
    logging.debug(f"Décodage de la chaîne de caractères '{source}'")
    logging.debug(f"Fichier de sortie : {args.output}" if args.output else "Pas de fichier de sortie")

    # Decoding process
    decode_base64(source, args.output)
