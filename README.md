# Gator Taxi

The UF Ride Network is a robust ride-sharing application designed to handle up to 2000 active ride requests. It supports essential features such as search, booking, cancellation, and updates.

## Features

- **Active Ride Management**: Efficiently handles up to 2000 active ride requests.
- **Search and Booking**: Allows users to search for available rides and book them seamlessly.
- **Cancellation and Updates**: Enables users to cancel their rides and update ride details as needed.

## Technical Implementation

### Data Structures

1. **Min-Heap**:
   - Used to store ride details: `(rideNumber, rideCost, tripDuration)`.
   - Rides are ordered by `rideCost`.
   - In case two rides have the same `rideCost`, they are ordered by `tripDuration`.
   - Each `rideCost-tripDuration` combination is unique.

2. **Red-Black Tree**:
   - Used to store ride details: `(rideNumber, rideCost, tripDuration)`.
   - Rides are ordered by `rideNumber`.

## Advanced Data Structures Utilized

- **Min-Heap**:
  - Efficiently manages ride details ordered by cost and duration.
  - Optimizes search and retrieval operations based on ride cost and duration.

- **Red-Black Tree**:
  - Ensures balanced tree structure for efficient insertion, deletion, and lookup operations.
  - Orders rides by ride number for quick access and updates.

## Summary

The UF Ride Network leverages advanced data structures like Min-Heap and Red-Black Trees to efficiently manage and process ride requests, providing a seamless user experience for ride search, booking, cancellation, and updates.
