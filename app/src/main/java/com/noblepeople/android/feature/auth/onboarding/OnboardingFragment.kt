package com.noblepeople.android.feature.auth.onboarding

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.noblepeople.android.databinding.FragmentOnboardingBinding


class OnboardingFragment : Fragment() {

    private var binding: FragmentOnboardingBinding? = null


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val _binding = FragmentOnboardingBinding.inflate(inflater, container, false)
        binding = _binding
        setupClickListeners()
        return _binding.root
    }

    private fun setupClickListeners() {
        binding?.navigateToLogin?.setOnClickListener {

        }
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

    }

}