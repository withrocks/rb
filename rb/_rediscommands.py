# flake8: noqa

import sys
if sys.version_info >= (3,):
    long = int

COMMANDS = {'APPEND': {'arity': long(3),
            'flags': ['write', 'denyoom'],
            'key_spec': (1, 1, 1)},
 'AUTH': {'arity': long(2),
          'flags': ['readonly', 'noscript', 'loading', 'stale', 'fast'],
          'key_spec': (0, 0, 0)},
 'BGREWRITEAOF': {'arity': long(1),
                  'flags': ['readonly', 'admin'],
                  'key_spec': (0, 0, 0)},
 'BGSAVE': {'arity': long(1),
            'flags': ['readonly', 'admin'],
            'key_spec': (0, 0, 0)},
 'BITCOUNT': {'arity': -long(2),
              'flags': ['readonly'],
              'key_spec': (1, 1, 1)},
 'BITOP': {'arity': -long(4),
           'flags': ['write', 'denyoom'],
           'key_spec': (2, -1, 1)},
 'BITPOS': {'arity': -long(3), 'flags': ['readonly'], 'key_spec': (1, 1, 1)},
 'BLPOP': {'arity': -long(3),
           'flags': ['write', 'noscript'],
           'key_spec': (1, -2, 1)},
 'BRPOP': {'arity': -long(3),
           'flags': ['write', 'noscript'],
           'key_spec': (1, 1, 1)},
 'BRPOPLPUSH': {'arity': long(4),
                'flags': ['write', 'denyoom', 'noscript'],
                'key_spec': (1, 2, 1)},
 'CLIENT': {'arity': -long(2),
            'flags': ['readonly', 'admin'],
            'key_spec': (0, 0, 0)},
 'COMMAND': {'arity': long(0),
             'flags': ['readonly', 'loading', 'stale'],
             'key_spec': (0, 0, 0)},
 'CONFIG': {'arity': -long(2),
            'flags': ['readonly', 'admin', 'stale'],
            'key_spec': (0, 0, 0)},
 'DBSIZE': {'arity': long(1),
            'flags': ['readonly', 'fast'],
            'key_spec': (0, 0, 0)},
 'DEBUG': {'arity': -long(2),
           'flags': ['admin', 'noscript'],
           'key_spec': (0, 0, 0)},
 'DECR': {'arity': long(2),
          'flags': ['write', 'denyoom', 'fast'],
          'key_spec': (1, 1, 1)},
 'DECRBY': {'arity': long(3),
            'flags': ['write', 'denyoom', 'fast'],
            'key_spec': (1, 1, 1)},
 'DEL': {'arity': -long(2), 'flags': ['write'], 'key_spec': (1, -1, 1)},
 'DISCARD': {'arity': long(1),
             'flags': ['readonly', 'noscript', 'fast'],
             'key_spec': (0, 0, 0)},
 'DUMP': {'arity': long(2),
          'flags': ['readonly', 'admin'],
          'key_spec': (1, 1, 1)},
 'ECHO': {'arity': long(2),
          'flags': ['readonly', 'fast'],
          'key_spec': (0, 0, 0)},
 'EVAL': {'arity': -long(3),
          'flags': ['noscript', 'movablekeys'],
          'key_spec': (0, 0, 0)},
 'EVALSHA': {'arity': -long(3),
             'flags': ['noscript', 'movablekeys'],
             'key_spec': (0, 0, 0)},
 'EXEC': {'arity': long(1),
          'flags': ['noscript', 'skip_monitor'],
          'key_spec': (0, 0, 0)},
 'EXISTS': {'arity': long(2),
            'flags': ['readonly', 'fast'],
            'key_spec': (1, 1, 1)},
 'EXPIRE': {'arity': long(3),
            'flags': ['write', 'fast'],
            'key_spec': (1, 1, 1)},
 'EXPIREAT': {'arity': long(3),
              'flags': ['write', 'fast'],
              'key_spec': (1, 1, 1)},
 'FLUSHALL': {'arity': long(1), 'flags': ['write'], 'key_spec': (0, 0, 0)},
 'FLUSHDB': {'arity': long(1), 'flags': ['write'], 'key_spec': (0, 0, 0)},
 'GET': {'arity': long(2),
         'flags': ['readonly', 'fast'],
         'key_spec': (1, 1, 1)},
 'GETBIT': {'arity': long(3),
            'flags': ['readonly', 'fast'],
            'key_spec': (1, 1, 1)},
 'GETRANGE': {'arity': long(4), 'flags': ['readonly'], 'key_spec': (1, 1, 1)},
 'GETSET': {'arity': long(3),
            'flags': ['write', 'denyoom'],
            'key_spec': (1, 1, 1)},
 'HDEL': {'arity': -long(3),
          'flags': ['write', 'fast'],
          'key_spec': (1, 1, 1)},
 'HEXISTS': {'arity': long(3),
             'flags': ['readonly', 'fast'],
             'key_spec': (1, 1, 1)},
 'HGET': {'arity': long(3),
          'flags': ['readonly', 'fast'],
          'key_spec': (1, 1, 1)},
 'HGETALL': {'arity': long(2), 'flags': ['readonly'], 'key_spec': (1, 1, 1)},
 'HINCRBY': {'arity': long(4),
             'flags': ['write', 'denyoom', 'fast'],
             'key_spec': (1, 1, 1)},
 'HINCRBYFLOAT': {'arity': long(4),
                  'flags': ['write', 'denyoom', 'fast'],
                  'key_spec': (1, 1, 1)},
 'HKEYS': {'arity': long(2),
           'flags': ['readonly', 'sort_for_script'],
           'key_spec': (1, 1, 1)},
 'HLEN': {'arity': long(2),
          'flags': ['readonly', 'fast'],
          'key_spec': (1, 1, 1)},
 'HMGET': {'arity': -long(3), 'flags': ['readonly'], 'key_spec': (1, 1, 1)},
 'HMSET': {'arity': -long(4),
           'flags': ['write', 'denyoom'],
           'key_spec': (1, 1, 1)},
 'HSCAN': {'arity': -long(3),
           'flags': ['readonly', 'random'],
           'key_spec': (1, 1, 1)},
 'HSET': {'arity': long(4),
          'flags': ['write', 'denyoom', 'fast'],
          'key_spec': (1, 1, 1)},
 'HSETNX': {'arity': long(4),
            'flags': ['write', 'denyoom', 'fast'],
            'key_spec': (1, 1, 1)},
 'HVALS': {'arity': long(2),
           'flags': ['readonly', 'sort_for_script'],
           'key_spec': (1, 1, 1)},
 'INCR': {'arity': long(2),
          'flags': ['write', 'denyoom', 'fast'],
          'key_spec': (1, 1, 1)},
 'INCRBY': {'arity': long(3),
            'flags': ['write', 'denyoom', 'fast'],
            'key_spec': (1, 1, 1)},
 'INCRBYFLOAT': {'arity': long(3),
                 'flags': ['write', 'denyoom', 'fast'],
                 'key_spec': (1, 1, 1)},
 'INFO': {'arity': -long(1),
          'flags': ['readonly', 'loading', 'stale'],
          'key_spec': (0, 0, 0)},
 'KEYS': {'arity': long(2),
          'flags': ['readonly', 'sort_for_script'],
          'key_spec': (0, 0, 0)},
 'LASTSAVE': {'arity': long(1),
              'flags': ['readonly', 'random', 'fast'],
              'key_spec': (0, 0, 0)},
 'LATENCY': {'arity': -long(2),
             'flags': ['readonly',
                       'admin',
                       'noscript',
                       'loading',
                       'stale'],
             'key_spec': (0, 0, 0)},
 'LINDEX': {'arity': long(3), 'flags': ['readonly'], 'key_spec': (1, 1, 1)},
 'LINSERT': {'arity': long(5),
             'flags': ['write', 'denyoom'],
             'key_spec': (1, 1, 1)},
 'LLEN': {'arity': long(2),
          'flags': ['readonly', 'fast'],
          'key_spec': (1, 1, 1)},
 'LPOP': {'arity': long(2),
          'flags': ['write', 'fast'],
          'key_spec': (1, 1, 1)},
 'LPUSH': {'arity': -long(3),
           'flags': ['write', 'denyoom', 'fast'],
           'key_spec': (1, 1, 1)},
 'LPUSHX': {'arity': long(3),
            'flags': ['write', 'denyoom', 'fast'],
            'key_spec': (1, 1, 1)},
 'LRANGE': {'arity': long(4), 'flags': ['readonly'], 'key_spec': (1, 1, 1)},
 'LREM': {'arity': long(4), 'flags': ['write'], 'key_spec': (1, 1, 1)},
 'LSET': {'arity': long(4),
          'flags': ['write', 'denyoom'],
          'key_spec': (1, 1, 1)},
 'LTRIM': {'arity': long(4), 'flags': ['write'], 'key_spec': (1, 1, 1)},
 'MGET': {'arity': -long(2), 'flags': ['readonly'], 'key_spec': (1, -1, 1)},
 'MIGRATE': {'arity': long(6),
             'flags': ['write', 'admin'],
             'key_spec': (0, 0, 0)},
 'MONITOR': {'arity': long(1),
             'flags': ['readonly', 'admin', 'noscript'],
             'key_spec': (0, 0, 0)},
 'MOVE': {'arity': long(3),
          'flags': ['write', 'fast'],
          'key_spec': (1, 1, 1)},
 'MSET': {'arity': -long(3),
          'flags': ['write', 'denyoom'],
          'key_spec': (1, -1, 2)},
 'MSETNX': {'arity': -long(3),
            'flags': ['write', 'denyoom'],
            'key_spec': (1, -1, 2)},
 'MULTI': {'arity': long(1),
           'flags': ['readonly', 'noscript', 'fast'],
           'key_spec': (0, 0, 0)},
 'OBJECT': {'arity': long(3), 'flags': ['readonly'], 'key_spec': (2, 2, 2)},
 'PERSIST': {'arity': long(2),
             'flags': ['write', 'fast'],
             'key_spec': (1, 1, 1)},
 'PEXPIRE': {'arity': long(3),
             'flags': ['write', 'fast'],
             'key_spec': (1, 1, 1)},
 'PEXPIREAT': {'arity': long(3),
               'flags': ['write', 'fast'],
               'key_spec': (1, 1, 1)},
 'PFADD': {'arity': -long(2),
           'flags': ['write', 'denyoom', 'fast'],
           'key_spec': (1, 1, 1)},
 'PFCOUNT': {'arity': -long(2), 'flags': ['write'], 'key_spec': (1, 1, 1)},
 'PFDEBUG': {'arity': -long(3), 'flags': ['write'], 'key_spec': (0, 0, 0)},
 'PFMERGE': {'arity': -long(2),
             'flags': ['write', 'denyoom'],
             'key_spec': (1, -1, 1)},
 'PFSELFTEST': {'arity': long(1),
                'flags': ['readonly'],
                'key_spec': (0, 0, 0)},
 'PING': {'arity': long(1),
          'flags': ['readonly', 'stale', 'fast'],
          'key_spec': (0, 0, 0)},
 'PSETEX': {'arity': long(4),
            'flags': ['write', 'denyoom'],
            'key_spec': (1, 1, 1)},
 'PSUBSCRIBE': {'arity': -long(2),
                'flags': ['readonly',
                          'pubsub',
                          'noscript',
                          'loading',
                          'stale'],
                'key_spec': (0, 0, 0)},
 'PSYNC': {'arity': long(3),
           'flags': ['readonly', 'admin', 'noscript'],
           'key_spec': (0, 0, 0)},
 'PTTL': {'arity': long(2),
          'flags': ['readonly', 'fast'],
          'key_spec': (1, 1, 1)},
 'PUBLISH': {'arity': long(3),
             'flags': ['readonly',
                       'pubsub',
                       'loading',
                       'stale',
                       'fast'],
             'key_spec': (0, 0, 0)},
 'PUBSUB': {'arity': -long(2),
            'flags': ['readonly',
                      'pubsub',
                      'random',
                      'loading',
                      'stale'],
            'key_spec': (0, 0, 0)},
 'PUNSUBSCRIBE': {'arity': -long(1),
                  'flags': ['readonly',
                            'pubsub',
                            'noscript',
                            'loading',
                            'stale'],
                  'key_spec': (0, 0, 0)},
 'RANDOMKEY': {'arity': long(1),
               'flags': ['readonly', 'random'],
               'key_spec': (0, 0, 0)},
 'RENAME': {'arity': long(3), 'flags': ['write'], 'key_spec': (1, 2, 1)},
 'RENAMENX': {'arity': long(3),
              'flags': ['write', 'fast'],
              'key_spec': (1, 2, 1)},
 'REPLCONF': {'arity': -long(1),
              'flags': ['readonly',
                        'admin',
                        'noscript',
                        'loading',
                        'stale'],
              'key_spec': (0, 0, 0)},
 'RESTORE': {'arity': long(4),
             'flags': ['write', 'denyoom', 'admin'],
             'key_spec': (1, 1, 1)},
 'ROLE': {'arity': long(1),
          'flags': ['admin', 'noscript', 'loading', 'stale'],
          'key_spec': (0, 0, 0)},
 'RPOP': {'arity': long(2),
          'flags': ['write', 'fast'],
          'key_spec': (1, 1, 1)},
 'RPOPLPUSH': {'arity': long(3),
               'flags': ['write', 'denyoom'],
               'key_spec': (1, 2, 1)},
 'RPUSH': {'arity': -long(3),
           'flags': ['write', 'denyoom', 'fast'],
           'key_spec': (1, 1, 1)},
 'RPUSHX': {'arity': long(3),
            'flags': ['write', 'denyoom', 'fast'],
            'key_spec': (1, 1, 1)},
 'SADD': {'arity': -long(3),
          'flags': ['write', 'denyoom', 'fast'],
          'key_spec': (1, 1, 1)},
 'SAVE': {'arity': long(1),
          'flags': ['readonly', 'admin', 'noscript'],
          'key_spec': (0, 0, 0)},
 'SCAN': {'arity': -long(2),
          'flags': ['readonly', 'random'],
          'key_spec': (0, 0, 0)},
 'SCARD': {'arity': long(2),
           'flags': ['readonly', 'fast'],
           'key_spec': (1, 1, 1)},
 'SCRIPT': {'arity': -long(2),
            'flags': ['readonly', 'admin', 'noscript'],
            'key_spec': (0, 0, 0)},
 'SDIFF': {'arity': -long(2),
           'flags': ['readonly', 'sort_for_script'],
           'key_spec': (1, -1, 1)},
 'SDIFFSTORE': {'arity': -long(3),
                'flags': ['write', 'denyoom'],
                'key_spec': (1, -1, 1)},
 'SELECT': {'arity': long(2),
            'flags': ['readonly', 'loading', 'fast'],
            'key_spec': (0, 0, 0)},
 'SET': {'arity': -long(3),
         'flags': ['write', 'denyoom'],
         'key_spec': (1, 1, 1)},
 'SETBIT': {'arity': long(4),
            'flags': ['write', 'denyoom'],
            'key_spec': (1, 1, 1)},
 'SETEX': {'arity': long(4),
           'flags': ['write', 'denyoom'],
           'key_spec': (1, 1, 1)},
 'SETNX': {'arity': long(3),
           'flags': ['write', 'denyoom', 'fast'],
           'key_spec': (1, 1, 1)},
 'SETRANGE': {'arity': long(4),
              'flags': ['write', 'denyoom'],
              'key_spec': (1, 1, 1)},
 'SHUTDOWN': {'arity': -long(1),
              'flags': ['readonly', 'admin', 'loading', 'stale'],
              'key_spec': (0, 0, 0)},
 'SINTER': {'arity': -long(2),
            'flags': ['readonly', 'sort_for_script'],
            'key_spec': (1, -1, 1)},
 'SINTERSTORE': {'arity': -long(3),
                 'flags': ['write', 'denyoom'],
                 'key_spec': (1, -1, 1)},
 'SISMEMBER': {'arity': long(3),
               'flags': ['readonly', 'fast'],
               'key_spec': (1, 1, 1)},
 'SLAVEOF': {'arity': long(3),
             'flags': ['admin', 'noscript', 'stale'],
             'key_spec': (0, 0, 0)},
 'SLOWLOG': {'arity': -long(2), 'flags': ['readonly'], 'key_spec': (0, 0, 0)},
 'SMEMBERS': {'arity': long(2),
              'flags': ['readonly', 'sort_for_script'],
              'key_spec': (1, 1, 1)},
 'SMOVE': {'arity': long(4),
           'flags': ['write', 'fast'],
           'key_spec': (1, 2, 1)},
 'SORT': {'arity': -long(2),
          'flags': ['write', 'denyoom'],
          'key_spec': (1, 1, 1)},
 'SPOP': {'arity': long(2),
          'flags': ['write', 'noscript', 'random', 'fast'],
          'key_spec': (1, 1, 1)},
 'SRANDMEMBER': {'arity': -long(2),
                 'flags': ['readonly', 'random'],
                 'key_spec': (1, 1, 1)},
 'SREM': {'arity': -long(3),
          'flags': ['write', 'fast'],
          'key_spec': (1, 1, 1)},
 'SSCAN': {'arity': -long(3),
           'flags': ['readonly', 'random'],
           'key_spec': (1, 1, 1)},
 'STRLEN': {'arity': long(2),
            'flags': ['readonly', 'fast'],
            'key_spec': (1, 1, 1)},
 'SUBSCRIBE': {'arity': -long(2),
               'flags': ['readonly',
                         'pubsub',
                         'noscript',
                         'loading',
                         'stale'],
               'key_spec': (0, 0, 0)},
 'SUBSTR': {'arity': long(4), 'flags': ['readonly'], 'key_spec': (1, 1, 1)},
 'SUNION': {'arity': -long(2),
            'flags': ['readonly', 'sort_for_script'],
            'key_spec': (1, -1, 1)},
 'SUNIONSTORE': {'arity': -long(3),
                 'flags': ['write', 'denyoom'],
                 'key_spec': (1, -1, 1)},
 'SYNC': {'arity': long(1),
          'flags': ['readonly', 'admin', 'noscript'],
          'key_spec': (0, 0, 0)},
 'TIME': {'arity': long(1),
          'flags': ['readonly', 'random', 'fast'],
          'key_spec': (0, 0, 0)},
 'TTL': {'arity': long(2),
         'flags': ['readonly', 'fast'],
         'key_spec': (1, 1, 1)},
 'TYPE': {'arity': long(2),
          'flags': ['readonly', 'fast'],
          'key_spec': (1, 1, 1)},
 'UNSUBSCRIBE': {'arity': -long(1),
                 'flags': ['readonly',
                           'pubsub',
                           'noscript',
                           'loading',
                           'stale'],
                 'key_spec': (0, 0, 0)},
 'UNWATCH': {'arity': long(1),
             'flags': ['readonly', 'noscript', 'fast'],
             'key_spec': (0, 0, 0)},
 'WATCH': {'arity': -long(2),
           'flags': ['readonly', 'noscript', 'fast'],
           'key_spec': (1, -1, 1)},
 'ZADD': {'arity': -long(4),
          'flags': ['write', 'denyoom', 'fast'],
          'key_spec': (1, 1, 1)},
 'ZCARD': {'arity': long(2),
           'flags': ['readonly', 'fast'],
           'key_spec': (1, 1, 1)},
 'ZCOUNT': {'arity': long(4),
            'flags': ['readonly', 'fast'],
            'key_spec': (1, 1, 1)},
 'ZINCRBY': {'arity': long(4),
             'flags': ['write', 'denyoom', 'fast'],
             'key_spec': (1, 1, 1)},
 'ZINTERSTORE': {'arity': -long(4),
                 'flags': ['write', 'denyoom', 'movablekeys'],
                 'key_spec': (0, 0, 0)},
 'ZLEXCOUNT': {'arity': long(4),
               'flags': ['readonly', 'fast'],
               'key_spec': (1, 1, 1)},
 'ZRANGE': {'arity': -long(4), 'flags': ['readonly'], 'key_spec': (1, 1, 1)},
 'ZRANGEBYLEX': {'arity': -long(4),
                 'flags': ['readonly'],
                 'key_spec': (1, 1, 1)},
 'ZRANGEBYSCORE': {'arity': -long(4),
                   'flags': ['readonly'],
                   'key_spec': (1, 1, 1)},
 'ZRANK': {'arity': long(3),
           'flags': ['readonly', 'fast'],
           'key_spec': (1, 1, 1)},
 'ZREM': {'arity': -long(3),
          'flags': ['write', 'fast'],
          'key_spec': (1, 1, 1)},
 'ZREMRANGEBYLEX': {'arity': long(4),
                    'flags': ['write'],
                    'key_spec': (1, 1, 1)},
 'ZREMRANGEBYRANK': {'arity': long(4),
                     'flags': ['write'],
                     'key_spec': (1, 1, 1)},
 'ZREMRANGEBYSCORE': {'arity': long(4),
                      'flags': ['write'],
                      'key_spec': (1, 1, 1)},
 'ZREVRANGE': {'arity': -long(4),
               'flags': ['readonly'],
               'key_spec': (1, 1, 1)},
 'ZREVRANGEBYLEX': {'arity': -long(4),
                    'flags': ['readonly'],
                    'key_spec': (1, 1, 1)},
 'ZREVRANGEBYSCORE': {'arity': -long(4),
                      'flags': ['readonly'],
                      'key_spec': (1, 1, 1)},
 'ZREVRANK': {'arity': long(3),
              'flags': ['readonly', 'fast'],
              'key_spec': (1, 1, 1)},
 'ZSCAN': {'arity': -long(3),
           'flags': ['readonly', 'random'],
           'key_spec': (1, 1, 1)},
 'ZSCORE': {'arity': long(3),
            'flags': ['readonly', 'fast'],
            'key_spec': (1, 1, 1)},
 'ZUNIONSTORE': {'arity': -long(4),
                 'flags': ['write', 'denyoom', 'movablekeys'],
                 'key_spec': (0, 0, 0)}}


if __name__ == '__main__':
    import redis
    import pprint

    rv = {}
    for row in redis.Redis().execute_command('COMMAND'):
        cmd, arity, flags, first_key, last_key, step_count = row
        rv[cmd.upper()] = {
            'arity': arity,
            'flags': flags,
            'key_spec': (int(first_key), int(last_key), int(step_count)),
        }

    tail = []
    with open(__file__.rstrip('co'), 'r+') as f:
        for line in f:
            if line.strip() == "if __name__ == '__main__':":
                tail.append(line)
                tail.extend(f)
                break

        f.seek(0)
        f.truncate(0)
        f.write('# flake8: noqa\n\nCOMMANDS = %s\n\n\n%s' % (
            pprint.pformat(rv, width=74),
            ''.join(tail)))
