from typing import List


class BaselineProcessor:
    @staticmethod
    def mean(values: List[float]) -> float:
        total = sum(values)
        return total / len(values) if values else 0.0

    
    @staticmethod
    def std(values: List[float]) -> float:
        mu = BaselineProcessor.mean(values)
        variance = sum((x - mu) ** 2 for x in values) / len(values) if values else 0.0
        return variance ** 0.5

    @staticmethod
    def moving_average(values: List[float], window: int = 5) -> List[float]:
        if window <= 0 or window > len(values):
            return []
        return [
            BaselineProcessor.mean(values[i:i+window])
            for i in range(len(values) - window + 1)
        ]
