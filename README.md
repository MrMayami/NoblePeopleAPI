# NoblePeopleAPI
 This a restful api for NoblePeople Mobile Application
 
 # API LINK - https://nobles-people-api.herokuapp.com/

# API ENDPOINTS

LiveRadio - /radio
LiveTV - /tv
LiveMagazine - /magazine
LiveNews - /news
LiveUpcoming - /upcoming

# HOW TO USE API

GET LiveRadio - https://nobles-people-api.herokuapp.com/radio

GET LiveTV - https://nobles-people-api.herokuapp.com/tv

GET LiveNews - https://nobles-people-api.herokuapp.com/news

GET LiveUpcoming - https://nobles-people-api.herokuapp.com/upcoming

# HOW TO USE API WITH KOTLIN

Here's an example of a REST call with OkHttp : http://square.github.io/okhttp/

# build.gradle

```
dependencies {
    //...
    implementation 'com.squareup.okhttp3:okhttp:3.8.1'
}
```

# AndroidManifest.xml

```
<uses-permission android:name="android.permission.INTERNET" />
```

# MainActivity.kt

```
class MainActivity : AppCompatActivity() {

    private val client = OkHttpClient()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        run("https://api.github.com/users/Evin1-/repos")
    }

    fun run(url: String) {
        val request = Request.Builder()
                .url(url)
                .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {}
            override fun onResponse(call: Call, response: Response) = println(response.body()?.string())
        })
    }
}

```


# RESOURCE LINKS

Below are a few more complicated examples with other libraries:

* Network request in Kotlin with Retrofit: https://loopcupcakes.com/blog/network-call-using-retrofit
* Network request in Kotlin with Retrofit and coroutines: https://loopcupcakes.com/blog/network-retrofit-coroutines
* Network request in Kotlin with Dagger, RxJava, Retrofit in MVP: https://github.com/Evin1-/Kotlin-MVP-Dagger2-RxJava-Retrofit
