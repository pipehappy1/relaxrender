using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityStandardAssets.ImageEffects;

public class CameraBlurFunc : MonoBehaviour {
	[Range(0.0f, 10.0f)]
	public float maxBlurSize = 3.0f;
	[Range(0.0f, 10.0f)]
	public float blurSpeed = 0.1f;
	public float waitTime = 0.1f;
	public BlurOptimized blur;

	void Start () {
		blur = GetComponent<BlurOptimized> ();
	}

	void OnEnable(){
		EventManager.bluring += CamBlur;
		EventManager.disBluring += CamDisBlur;
	}

	void OnDisable(){
		EventManager.bluring -= CamBlur;
		EventManager.disBluring -= CamDisBlur;
	}

	public void CamBlur(){
		if (!blur.enabled) {
			StartCoroutine (CameraBlurCoroutine ());
		}
	}
	public void CamDisBlur(){
		if (blur.enabled) {
			StartCoroutine (CameraDisBlurCoroutine ());
		}
	}

	IEnumerator CameraBlurCoroutine(){
		blur.enabled = true;
		yield return null;
		while (blur.blurSize <= maxBlurSize) {
			blur.blurSize += blurSpeed;
			yield return new WaitForSecondsRealtime (waitTime);
		}
	}

	IEnumerator CameraDisBlurCoroutine(){
		while (blur.blurSize >= blurSpeed) {
			blur.blurSize -= blurSpeed;
			yield return new WaitForSecondsRealtime (waitTime);
		}
		blur.enabled = false;
		yield return null;
	}
}
