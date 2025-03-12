class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> (value, frequency)
        self.freq = {}   # frequency -> set of keys
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache:
            return -1  # No encontrado

        value, freq = self.cache[key]
        self.cache[key] = (value, freq + 1)

        # Actualizar frecuencia
        self.freq[freq].remove(key)
        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.freq.setdefault(freq + 1, set()).add(key)
        return value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)  # Actualizar frecuencia
            return

        if len(self.cache) >= self.capacity:
            # Eliminar el menos usado
            min_freq_keys = self.freq[self.min_freq]
            evict_key = min_freq_keys.pop()
            if not min_freq_keys:
                del self.freq[self.min_freq]
            del self.cache[evict_key]

        self.cache[key] = (value, 1)
        self.freq.setdefault(1, set()).add(key)
        self.min_freq = 1