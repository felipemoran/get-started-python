import web_server
import time

# ============ LOCAL VARIABLES =========================================================================================

stats_dictionary = {
    "message_counter": 0,
    "last_message": 0,
    "last_message_ts": time.time(),
    "start_time": time.time()
}

# ============ MAIN ====================================================================================================

if __name__ == '__main__':
    web_server.stats_dictionary = stats_dictionary
    web_server.run()

    # parser = charlie_parser.Parser(stats_dictionary)
    # parser.run()

    print("I guess it's the end of times... at least for this program")
