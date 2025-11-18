<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");
header("Content-Type: application/json");

$API_KEY = "AIzaSyB12M3tR7J9R9HoHKB9SHwbEJHf2I4pM10";  // Replace with your real API key
$MODEL   = "gemini-2.5-flash";

// Build URL to Google API
$url = "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent?key=$API_KEY";

// Receive JSON from InfinityFree
$payload = file_get_contents("php://input");

// Prepare HTTP request to forward to Google API
$context = stream_context_create([
    "http" => [
        "method"  => "POST",
        "header"  => "Content-Type: application/json",
        "content" => $payload
    ]
]);

// Send the request and get the response from Google AI
$response = file_get_contents($url, false, $context);

// Return response to InfinityFree
echo $response;
