import numpy as np
import torch

import os.path as osp
from .custom import CustomDataset

CLASS_LABELS_200 = (
        'wall', 'chair', 'floor', 'table', 'door', 'couch', 'cabinet', 'shelf', 'desk', 'office chair', 'bed', 'pillow', 'sink', 'picture', 'window', 'toilet', 'bookshelf', 'monitor', 'curtain', 'book', 'armchair', 'coffee table', 'box',
        'refrigerator', 'lamp', 'kitchen cabinet', 'towel', 'clothes', 'tv', 'nightstand', 'counter', 'dresser', 'stool', 'cushion', 'plant', 'ceiling', 'bathtub', 'end table', 'dining table', 'keyboard', 'bag', 'backpack', 'toilet paper',
        'printer', 'tv stand', 'whiteboard', 'blanket', 'shower curtain', 'trash can', 'closet', 'stairs', 'microwave', 'stove', 'shoe', 'computer tower', 'bottle', 'bin', 'ottoman', 'bench', 'board', 'washing machine', 'mirror', 'copier',
        'basket', 'sofa chair', 'file cabinet', 'fan', 'laptop', 'shower', 'paper', 'person', 'paper towel dispenser', 'oven', 'blinds', 'rack', 'plate', 'blackboard', 'piano', 'suitcase', 'rail', 'radiator', 'recycling bin', 'container',
        'wardrobe', 'soap dispenser', 'telephone', 'bucket', 'clock', 'stand', 'light', 'laundry basket', 'pipe', 'clothes dryer', 'guitar', 'toilet paper holder', 'seat', 'speaker', 'column', 'bicycle', 'ladder', 'bathroom stall', 'shower wall',
        'cup', 'jacket', 'storage bin', 'coffee maker', 'dishwasher', 'paper towel roll', 'machine', 'mat', 'windowsill', 'bar', 'toaster', 'bulletin board', 'ironing board', 'fireplace', 'soap dish', 'kitchen counter', 'doorframe',
        'toilet paper dispenser', 'mini fridge', 'fire extinguisher', 'ball', 'hat', 'shower curtain rod', 'water cooler', 'paper cutter', 'tray', 'shower door', 'pillar', 'ledge', 'toaster oven', 'mouse', 'toilet seat cover dispenser',
        'furniture', 'cart', 'storage container', 'scale', 'tissue box', 'light switch', 'crate', 'power outlet', 'decoration', 'sign', 'projector', 'closet door', 'vacuum cleaner', 'candle', 'plunger', 'stuffed animal', 'headphones', 'dish rack',
        'broom', 'guitar case', 'range hood', 'dustpan', 'hair dryer', 'water bottle', 'handicap bar', 'purse', 'vent', 'shower floor', 'water pitcher', 'mailbox', 'bowl', 'paper bag', 'alarm clock', 'music stand', 'projector screen', 'divider',
        'laundry detergent', 'bathroom counter', 'object', 'bathroom vanity', 'closet wall', 'laundry hamper', 'bathroom stall door', 'ceiling light', 'trash bin', 'dumbbell', 'stair rail', 'tube', 'bathroom cabinet', 'cd case', 'closet rod',
        'coffee kettle', 'structure', 'shower head', 'keyboard piano', 'case of water bottles', 'coat rack', 'storage organizer', 'folded chair', 'fire alarm', 'power strip', 'calendar', 'poster', 'potted plant', 'luggage', 'mattress'
    )

# CLASSES = [CLASS_LABELS_200[i] for i in BENCHMARK_SEMANTIC_IDXS[2:]]


class ScanNet200Dataset(CustomDataset):
    BENCHMARK_SEMANTIC_IDXS = np.load('dataset/scannet200/reverse_norm_ids.npy')

    CLASSES = ('chair', 'table', 'door', 'couch', 'cabinet', 'shelf', 'desk', 'office chair', 'bed', 'pillow', 'sink', 'picture', 'window', 'toilet', 'bookshelf', 'monitor', 'curtain', 'book', 'armchair', 'coffee table', 'box',
        'refrigerator', 'lamp', 'kitchen cabinet', 'towel', 'clothes', 'tv', 'nightstand', 'counter', 'dresser', 'stool', 'cushion', 'plant', 'ceiling', 'bathtub', 'end table', 'dining table', 'keyboard', 'bag', 'backpack', 'toilet paper',
        'printer', 'tv stand', 'whiteboard', 'blanket', 'shower curtain', 'trash can', 'closet', 'stairs', 'microwave', 'stove', 'shoe', 'computer tower', 'bottle', 'bin', 'ottoman', 'bench', 'board', 'washing machine', 'mirror', 'copier',
        'basket', 'sofa chair', 'file cabinet', 'fan', 'laptop', 'shower', 'paper', 'person', 'paper towel dispenser', 'oven', 'blinds', 'rack', 'plate', 'blackboard', 'piano', 'suitcase', 'rail', 'radiator', 'recycling bin', 'container',
        'wardrobe', 'soap dispenser', 'telephone', 'bucket', 'clock', 'stand', 'light', 'laundry basket', 'pipe', 'clothes dryer', 'guitar', 'toilet paper holder', 'seat', 'speaker', 'column', 'bicycle', 'ladder', 'bathroom stall', 'shower wall',
        'cup', 'jacket', 'storage bin', 'coffee maker', 'dishwasher', 'paper towel roll', 'machine', 'mat', 'windowsill', 'bar', 'toaster', 'bulletin board', 'ironing board', 'fireplace', 'soap dish', 'kitchen counter', 'doorframe',
        'toilet paper dispenser', 'mini fridge', 'fire extinguisher', 'ball', 'hat', 'shower curtain rod', 'water cooler', 'paper cutter', 'tray', 'shower door', 'pillar', 'ledge', 'toaster oven', 'mouse', 'toilet seat cover dispenser',
        'furniture', 'cart', 'storage container', 'scale', 'tissue box', 'light switch', 'crate', 'power outlet', 'decoration', 'sign', 'projector', 'closet door', 'vacuum cleaner', 'candle', 'plunger', 'stuffed animal', 'headphones', 'dish rack',
        'broom', 'guitar case', 'range hood', 'dustpan', 'hair dryer', 'water bottle', 'handicap bar', 'purse', 'vent', 'shower floor', 'water pitcher', 'mailbox', 'bowl', 'paper bag', 'alarm clock', 'music stand', 'projector screen', 'divider',
        'laundry detergent', 'bathroom counter', 'object', 'bathroom vanity', 'closet wall', 'laundry hamper', 'bathroom stall door', 'ceiling light', 'trash bin', 'dumbbell', 'stair rail', 'tube', 'bathroom cabinet', 'cd case', 'closet rod',
        'coffee kettle', 'structure', 'shower head', 'keyboard piano', 'case of water bottles', 'coat rack', 'storage organizer', 'folded chair', 'fire alarm', 'power strip', 'calendar', 'poster', 'potted plant', 'luggage', 'mattress'
    )

    HEAD_CATS_SCANNET_200 = ['tv stand', 'curtain', 'blinds', 'shower curtain', 'bookshelf', 'tv', 'kitchen cabinet', 'pillow', 'lamp', 'dresser', 'monitor', 'object', 'ceiling', 'board', 'stove', 'closet wall', 'couch', 'office chair', 'kitchen counter', 'shower', 'closet', 'doorframe', 'sofa chair', 'mailbox', 'nightstand', 'washing machine', 'picture', 'book', 'sink', 'recycling bin', 'table', 'backpack', 'shower wall', 'toilet', 'copier', 'counter', 'stool', 'refrigerator', 'window', 'file cabinet', 'chair', 'wall', 'plant', 'coffee table', 'stairs', 'armchair', 'cabinet', 'bathroom vanity', 'bathroom stall', 'mirror', 'blackboard', 'trash can', 'stair rail', 'box', 'towel', 'door', 'clothes', 'whiteboard', 'bed', 'floor', 'bathtub', 'desk', 'wardrobe', 'clothes dryer', 'radiator', 'shelf']
    COMMON_CATS_SCANNET_200 = ["cushion", "end table", "dining table", "keyboard", "bag", "toilet paper", "printer", "blanket", "microwave", "shoe", "computer tower", "bottle", "bin", "ottoman", "bench", "basket", "fan", "laptop", "person", "paper towel dispenser", "oven", "rack", "piano", "suitcase", "rail", "container", "telephone", "stand", "light", "laundry basket", "pipe", "seat", "column", "bicycle", "ladder", "jacket", "storage bin", "coffee maker", "dishwasher", "machine", "mat", "windowsill", "bulletin board", "fireplace", "mini fridge", "water cooler", "shower door", "pillar", "ledge", "furniture", "cart", "decoration", "closet door", "vacuum cleaner", "dish rack", "range hood", "projector screen", "divider", "bathroom counter", "laundry hamper", "bathroom stall door", "ceiling light", "trash bin", "bathroom cabinet", "structure", "storage organizer", "potted plant", "mattress"]
    TAIL_CATS_SCANNET_200 = ["paper", "plate", "soap dispenser", "bucket", "clock", "guitar", "toilet paper holder", "speaker", "cup", "paper towel roll", "bar", "toaster", "ironing board", "soap dish", "toilet paper dispenser", "fire extinguisher", "ball", "hat", "shower curtain rod", "paper cutter", "tray", "toaster oven", "mouse", "toilet seat cover dispenser", "storage container", "scale", "tissue box", "light switch", "crate", "power outlet", "sign", "projector", "candle", "plunger", "stuffed animal", "headphones", "broom", "guitar case", "dustpan", "hair dryer", "water bottle", "handicap bar", "purse", "vent", "shower floor", "water pitcher", "bowl", "paper bag", "alarm clock", "music stand", "laundry detergent", "dumbbell", "tube", "cd case", "closet rod", "coffee kettle", "shower head", "keyboard piano", "case of water bottles", "coat rack", "folded chair", "fire alarm", "power strip", "calendar", "poster", "luggage"]
    VALID_CLASS_IDS_200_VALIDATION = ('wall', 'chair', 'floor', 'table', 'door', 'couch', 'cabinet', 'shelf', 'desk', 'office chair', 'bed', 'pillow', 'sink', 'picture', 'window', 'toilet', 'bookshelf', 'monitor', 'curtain', 'book', 'armchair', 'coffee table', 'box', 'refrigerator', 'lamp', 'kitchen cabinet', 'towel', 'clothes', 'tv', 'nightstand', 'counter', 'dresser', 'stool', 'cushion', 'plant', 'ceiling', 'bathtub', 'end table', 'dining table', 'keyboard', 'bag', 'backpack', 'toilet paper', 'printer', 'tv stand', 'whiteboard', 'blanket', 'shower curtain', 'trash can', 'closet', 'stairs', 'microwave', 'stove', 'shoe', 'computer tower', 'bottle', 'bin', 'ottoman', 'bench', 'board', 'washing machine', 'mirror', 'copier', 'basket', 'sofa chair', 'file cabinet', 'fan', 'laptop', 'shower', 'paper', 'person', 'paper towel dispenser', 'oven', 'blinds', 'rack', 'plate', 'blackboard', 'piano', 'suitcase', 'rail', 'radiator', 'recycling bin', 'container', 'wardrobe', 'soap dispenser', 'telephone', 'bucket', 'clock', 'stand', 'light', 'laundry basket', 'pipe', 'clothes dryer', 'guitar', 'toilet paper holder', 'seat', 'speaker', 'column', 'ladder', 'bathroom stall', 'shower wall', 'cup', 'jacket', 'storage bin', 'coffee maker', 'dishwasher', 'paper towel roll', 'machine', 'mat', 'windowsill', 'bar', 'toaster', 'bulletin board', 'ironing board', 'fireplace', 'soap dish', 'kitchen counter', 'doorframe', 'toilet paper dispenser', 'mini fridge', 'fire extinguisher', 'ball', 'hat', 'shower curtain rod', 'water cooler', 'paper cutter', 'tray', 'shower door', 'pillar', 'ledge', 'toaster oven', 'mouse', 'toilet seat cover dispenser', 'furniture', 'cart', 'scale', 'tissue box', 'light switch', 'crate', 'power outlet', 'decoration', 'sign', 'projector', 'closet door', 'vacuum cleaner', 'plunger', 'stuffed animal', 'headphones', 'dish rack', 'broom', 'range hood', 'dustpan', 'hair dryer', 'water bottle', 'handicap bar', 'vent', 'shower floor', 'water pitcher', 'mailbox', 'bowl', 'paper bag', 'projector screen', 'divider', 'laundry detergent', 'bathroom counter', 'object', 'bathroom vanity', 'closet wall', 'laundry hamper', 'bathroom stall door', 'ceiling light', 'trash bin', 'dumbbell', 'stair rail', 'tube', 'bathroom cabinet', 'closet rod', 'coffee kettle', 'shower head', 'keyboard piano', 'case of water bottles', 'coat rack', 'folded chair', 'fire alarm', 'power strip', 'calendar', 'poster', 'potted plant', 'mattress')




    def load(self, filename):
        scan_id = osp.basename(filename).replace(self.suffix, "")

        if self.prefix == "test":
            xyz, rgb = self.load(filename)
            semantic_label = np.zeros(xyz.shape[0], dtype=np.long)
            instance_label = np.zeros(xyz.shape[0], dtype=np.long)
        else:
            xyz, rgb, semantic_label, instance_label = torch.load(filename)

        spp_filename = osp.join(self.data_root, "superpoints", scan_id + ".pth")
        spp = torch.load(spp_filename)

        # FIXME
        # if np.max(rgb) > 10.0:
        rgb = rgb.astype(np.float32) / 127.5 - 1.0

        instance_label[semantic_label <= 1] = -100
        return xyz, rgb, semantic_label, instance_label, spp