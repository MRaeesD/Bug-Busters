prevnode = node;
//Change made here
                node.setSuccessor(prevnode);
                node = nextnode;
        }
        return prevnode;
    }
}
