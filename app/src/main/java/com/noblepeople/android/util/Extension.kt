package com.noblepeople.android.util

import android.widget.ImageView
import androidx.annotation.DrawableRes
import com.bumptech.glide.Glide

/**
 * File contains all the extension functions required for the project
 */

fun ImageView.loadImage(url: String) {
    Glide.with(this).load(url).into(this)
}

fun ImageView.loadImage(@DrawableRes drawable: Int) {
    Glide.with(this).load(drawable).into(this)
}
