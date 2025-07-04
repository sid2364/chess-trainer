import json
import argparse


def traverse(node: dict, move_sequence: list[str], depth: int) -> None:
    opening_name = node.get('opening_name')
    if opening_name:
        moves_san = ' '.join(move_sequence)
        indent = '  ' * depth
        print(f"{indent}{moves_san} - {opening_name}")

    for uci, child in node.get('children', {}).items():
        traverse(child, move_sequence + [uci], depth + 1)


def main(json_path: str) -> None:
    # Load the serialized trie
    with open(json_path, 'r', encoding='utf-8') as f:
        trie = json.load(f)

    # Start traversal from the root; empty move sequence and depth 0
    traverse(trie, [], 0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='print opening-book trie in human-readable form just fo debugging')
    parser.add_argument('json', help='Path to opening_book.json')
    args = parser.parse_args()
    main(args.json)
