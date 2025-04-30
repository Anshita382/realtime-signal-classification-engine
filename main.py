import argparse
from edad.consumer import consume_messages

def main():
    parser = argparse.ArgumentParser(description='UFO Signal Analyzer')
    parser.add_argument('--command', required=True, help='Hostname of RabbitMQ server')
    parser.add_argument('--port', type=int, required=True, help='Port number of RabbitMQ server')
    args = parser.parse_args()
    consume_messages(args.command, args.port)

if __name__ == '__main__':
    main()
