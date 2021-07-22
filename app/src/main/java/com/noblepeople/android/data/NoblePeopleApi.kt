package com.noblepeople.android.data

import retrofit2.http.GET

interface NoblePeopleApi {

    @GET("domains")
    suspend fun ping()
}
