import unittest
from src.lfu_cache import LFUCache

class TestLFUCache(unittest.TestCase):
    def test_put_and_get(self):
        cache = LFUCache(2)
        cache.put(1, 'A')
        cache.put(2, 'B')

        self.assertEqual(cache.get(1), 'A')  # Hit
        cache.put(3, 'C')  # Esto debe eliminar el 2 (menos usado)

        self.assertEqual(cache.get(2), -1)  # Fallo esperado
        self.assertEqual(cache.get(3), 'C')  # Hit
        self.assertEqual(cache.get(1), 'A')  # Hit

    def test_eviction_policy(self):
        cache = LFUCache(2)
        cache.put(1, 'A')
        cache.put(2, 'B')
        cache.get(1)  # Ahora 1 tiene frecuencia 2
        cache.put(3, 'C')  # Esto debe eliminar el 2

        self.assertEqual(cache.get(2), -1)  # Fallo esperado
        self.assertEqual(cache.get(1), 'A')  # Hit
        self.assertEqual(cache.get(3), 'C')  # Hit

if __name__ == '__main__':
    unittest.main()