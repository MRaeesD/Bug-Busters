java
} else {
    for (Node successornodes : node.getSuccessors()) {
        if (search(successornodes)) {
            return true;
        }
    }
    return false; // Added return statement
}
