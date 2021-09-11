"""Parser for Match Cost Functions."""
import lark

mcf_parser = lark.Lark(r"""
    ?aggregate_expr: aggregate_term
                   | aggregate_expr "+" aggregate_term -> add
                   | aggregate_expr "-" aggregate_term -> subtract

    ?aggregate_term: aggregate
                   | aggregate_term "*" aggregate -> mul
                   | aggregate_term "/" aggregate -> div

    ?aggregate: "sum(" expr ")" -> sum
              | "avg(" expr ")" -> avg
              | "diff(" expr ")" -> diff
              | "-" aggregate -> negative
              | "(" aggregate_expr ")"
              | NUMBER -> number

    ?expr: term
         | expr "+" term
         | expr "-" term

    ?term: atom
         | term "*" atom
         | term "/" atom

    ?atom: NUMBER -> number
         | "-" atom -> negative_list
         | ATTRIBUTE -> attribute
         | "(" expr ")"

    %import common.CNAME -> ATTRIBUTE
    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
""", start='aggregate_expr')


class MatchCostFunctionTransformer(lark.Transformer):
    def __init__(self, attributes: dict[str, list[float]]):
        super().__init__()
        self._attributes = attributes

    def attribute(self, att: str) -> list[float]:
        (att,) = att
        if att not in self._attributes:
            raise ValueError(f'"{att}" is not a known attribute')
        return self._attributes[att]

    @staticmethod
    def add(x):
        left, right = x
        return left + right

    @staticmethod
    def subtract(x):
        left, right = x
        return left - right

    @staticmethod
    def mul(x):
        left, right = x
        return left * right

    @staticmethod
    def div(x):
        numerator, denominator = x
        return numerator / denominator

    @staticmethod
    def sum(xs: list[list[float]]) -> float:
        return sum(xs[0])

    @staticmethod
    def avg(xs: list[list[float]]) -> float:
        return sum(xs[0]) / len(xs[0])

    @staticmethod
    def diff(xs: list[list[float]]):
        return max(xs[0]) - min(xs[0])

    @staticmethod
    def number(n) -> float:
        return float(n[0])

    @staticmethod
    def negative(n) -> float:
        return -n[0]


if __name__ == "__main__":
    parse_tree = mcf_parser.parse('diff(ratings')
    t = MatchCostFunctionTransformer(attributes={
        'rating': [900, 1050],
        'wait_time': [10, 60],
    })
    print(parse_tree.pretty())
    result = t.transform(parse_tree)
    print(result)
