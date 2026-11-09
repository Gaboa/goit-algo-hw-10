import random

A = 0
B = 3


def f(x: float) -> float:
	return x**3 + 2 * x


def monte_carlo_integral(num_samples: int) -> float:
	random_gen = random.Random(42)
	max_y = f(B)
	hits = 0

	for _ in range(num_samples):
		x = random_gen.uniform(A, B)
		y = random_gen.uniform(0, max_y)
		if y <= f(x):
			hits += 1

	return (B - A) * max_y * hits / num_samples


if __name__ == "__main__":
	exact_integral = (B**4 / 4 + B**2) - (A**4 / 4 + A**2)
	print(f"Аналітичне значення інтеграла: {exact_integral:.6f}")

	for num_samples in (1_000, 10_000, 100_000):
		mc_integral = monte_carlo_integral(num_samples)
		print(
			f"N={num_samples:>6}: оцінка={mc_integral:.6f}, "
		)
