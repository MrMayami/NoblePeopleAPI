package com.noblepeople.android.feature.auth

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.noblepeople.android.databinding.ActivityAuthBinding

class AuthActivity : AppCompatActivity() {

    private val binding by lazy(LazyThreadSafetyMode.NONE) {
        ActivityAuthBinding.inflate(layoutInflater)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
    }
}
