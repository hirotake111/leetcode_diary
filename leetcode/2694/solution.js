class EventEmitter {
  constructor() {
    this.store = new Map();
  }

  subscribe(event, cb) {
    if (!this.store.has(event)) this.store.set(event, []);
    const listeners = this.store.get(event);
    const listener = { cb, enabled: true };
    listeners.push(listener);

    return {
      unsubscribe: () => {
        listener.enabled = false;
        return;
      },
    };
  }

  emit(event, args = []) {
    const listeners = this.store.get(event) || [];
    if (listeners === undefined) return [];
    return listeners.reduce((acc, listener) => {
      if (listener.enabled) acc.push(listener.cb(...args));
      return acc;
    }, []);
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
