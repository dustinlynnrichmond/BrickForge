plugins { id("com.android.application") }

android {
    namespace = "com.brickforge.theme"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.brickforge.theme"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "0.1.0"
    }

    buildTypes { release { isMinifyEnabled = false } }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}
